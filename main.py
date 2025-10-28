from flask import Flask, render_template, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import io
import base64
import os
import textwrap
from pillow_heif import register_heif_opener

register_heif_opener()
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

FONT_PATH = os.path.join(os.path.dirname(__file__), "fonts/ClashDisplay-Medium.otf")
FRAME_PATH = os.path.join(os.path.dirname(__file__), "dp.png")

try:
    FRAME = Image.open(FRAME_PATH).convert("RGBA")
    FRAME_WIDTH, FRAME_HEIGHT = FRAME.size
    BASE_FONT_SIZE = int(FRAME_WIDTH * 0.04)
    FONT = ImageFont.truetype(FONT_PATH, BASE_FONT_SIZE)
except Exception as e:
    print(f"Error loading resources: {e}")
    FRAME, FONT = None, None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process-image", methods=["POST"])
def process_image():
    if not FRAME or not FONT:
        return jsonify({"error": "Server resources not loaded"}), 500

    try:
        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400

        uploaded_file = request.files["image"]
        if uploaded_file.filename == "":
            return jsonify({"error": "No image selected"}), 400

        username = request.form.get("username", "").strip()
        if not username:
            return jsonify({"error": "Username is required"}), 400

        image_data = uploaded_file.read()
        user_image = Image.open(io.BytesIO(image_data))

        try:
            from PIL import ImageOps

            user_image = ImageOps.exif_transpose(user_image)
        except Exception:
            pass

        user_image = user_image.convert("RGBA")

        circle_diameter = int(FRAME_WIDTH * 0.395)
        user_image_resized = resize_and_crop(
            user_image, circle_diameter, circle_diameter
        )

        mask = create_circular_mask(circle_diameter)
        user_image_resized.putalpha(mask)

        result = FRAME.copy()
        paste_x = (FRAME_WIDTH - circle_diameter) // 2
        paste_y = int(FRAME_HEIGHT * 0.50) - (circle_diameter // 2)
        result.paste(user_image_resized, (paste_x, paste_y), user_image_resized)

        draw = ImageDraw.Draw(result)
        add_username_text(draw, username, FRAME_WIDTH, FRAME_HEIGHT)

        result_rgb = result.convert("RGB")

        img_io = io.BytesIO()
        result_rgb.save(img_io, "JPEG", quality=90, optimize=False)
        img_io.seek(0)

        img_base64 = base64.b64encode(img_io.getvalue()).decode("utf-8")

        return jsonify({"image": f"data:image/jpeg;base64,{img_base64}"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def resize_and_crop(image, target_width, target_height):
    max_dimension = 1024
    if image.width > max_dimension or image.height > max_dimension:
        image.thumbnail((max_dimension, max_dimension), Image.Resampling.BICUBIC)

    # Efficient cropping and resizing
    img_ratio = image.width / image.height
    target_ratio = target_width / target_height

    if img_ratio > target_ratio:
        new_width = int(img_ratio * target_height)
        new_height = target_height
    else:
        new_width = target_width
        new_height = int(target_width / img_ratio)

    image = image.resize((new_width, new_height), Image.Resampling.BICUBIC)

    left = int((new_width - target_width) / 2)
    top = int((new_height - target_height) / 2)
    right = int((new_width + target_width) / 2)
    bottom = int((new_height + target_height) / 2)

    return image.crop((left, top, right, bottom))


def create_circular_mask(size):
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    return mask


def add_username_text(draw, username, frame_width, frame_height):
    username = username.upper()
    text_box_width = int(frame_width * 0.4)

    # Adjust font size based on username length for better fit
    font_size = BASE_FONT_SIZE
    if len(username) > 15:
        font_size = int(BASE_FONT_SIZE * (15 / len(username)))

    font = FONT.font_variant(size=font_size)

    # Use textwrap for cleaner line breaking
    avg_char_width = sum(font.getbbox(c)[2] for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") / 26
    max_chars_per_line = int(text_box_width / avg_char_width)
    lines = textwrap.wrap(username, width=max_chars_per_line, break_long_words=True)

    if not lines:
        return

    # Calculate text position
    line_heights = [font.getbbox(line)[3] - font.getbbox(line)[1] for line in lines]
    total_text_height = sum(line_heights) + (len(lines) - 1) * int(font_size * 0.3)
    text_box_center_y = int(frame_height * 0.745)
    start_y = text_box_center_y - (total_text_height // 2)

    # Draw text line by line
    current_y = start_y
    for line, line_height in zip(lines, line_heights):
        text_width = font.getbbox(line)[2]
        text_x = (frame_width - text_width) // 2
        draw.text((text_x, current_y), line, fill=(0, 0, 0, 255), font=font)
        current_y += line_height + int(font_size * 0.3)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
