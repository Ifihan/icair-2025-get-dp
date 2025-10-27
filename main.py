from flask import Flask, render_template, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import io
import base64
import os

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process-image", methods=["POST"])
def process_image():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400

        uploaded_file = request.files["image"]
        if uploaded_file.filename == "":
            return jsonify({"error": "No image selected"}), 400

        username = request.form.get("username", "").strip()
        if not username:
            return jsonify({"error": "Username is required"}), 400

        user_image = Image.open(uploaded_file.stream).convert("RGBA")

        frame_path = os.path.join(os.path.dirname(__file__), "dp.png")
        frame = Image.open(frame_path).convert("RGBA")

        frame_width, frame_height = frame.size

        circle_center_x = frame_width // 2
        circle_center_y = int(frame_height * 0.525)
        circle_diameter = int(frame_width * 0.395)
        circle_radius = circle_diameter // 2

        user_image_resized = resize_and_crop(
            user_image, circle_diameter, circle_diameter
        )

        mask = create_circular_mask(circle_diameter)

        user_image_resized.putalpha(mask)

        result = frame.copy()

        paste_x = circle_center_x - circle_radius
        paste_y = circle_center_y - circle_radius
        result.paste(user_image_resized, (paste_x, paste_y), user_image_resized)

        draw = ImageDraw.Draw(result)
        add_username_text(draw, username, frame_width, frame_height)

        img_io = io.BytesIO()
        result.save(img_io, "PNG", quality=95)
        img_io.seek(0)

        img_base64 = base64.b64encode(img_io.getvalue()).decode("utf-8")

        return jsonify({"image": f"data:image/png;base64,{img_base64}"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def resize_and_crop(image, target_width, target_height):
    img_width, img_height = image.size
    target_ratio = target_width / target_height
    img_ratio = img_width / img_height

    if img_ratio > target_ratio:
        new_height = target_height
        new_width = int(img_width * (target_height / img_height))
    else:
        new_width = target_width
        new_height = int(img_height * (target_width / img_width))

    resized = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    left = (new_width - target_width) // 2
    top = (new_height - target_height) // 2
    right = left + target_width
    bottom = top + target_height

    return resized.crop((left, top, right, bottom))


def create_circular_mask(size):
    mask = Image.new("L", (size, size), 0)
    from PIL import ImageDraw

    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    return mask


def add_username_text(draw, username, frame_width, frame_height):
    username = username.upper()

    text_box_center_y = int(frame_height * 0.745)
    text_box_width = int(frame_width * 0.55)

    font_path = os.path.join(
        os.path.dirname(__file__),
        "fonts/ClashDisplay-Medium.otf",
    )

    base_font_size = int(frame_width * 0.055)
    font = ImageFont.truetype(font_path, base_font_size)

    text_bbox = draw.textbbox((0, 0), username, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    if text_width > text_box_width:
        scale_factor = text_box_width / text_width
        new_font_size = int(base_font_size * scale_factor * 0.95)
        font = ImageFont.truetype(font_path, new_font_size)
        text_bbox = draw.textbbox((0, 0), username, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

    text_x = (frame_width - text_width) // 2
    text_y = text_box_center_y - (text_height // 2)

    draw.text((text_x, text_y), username, fill=(0, 0, 0, 255), font=font)


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
