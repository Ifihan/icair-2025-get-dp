# Profile Picture Generator

A customizable web application that generates branded profile pictures for events, conferences, or communities. Users can upload their photo, add their name, and get a professionally framed profile picture ready to share on social media.

## Features

- Upload and process images (supports PNG, JPG, HEIC/HEIF)
- Automatic circular cropping and centering
- Custom text overlay with automatic sizing
- Responsive design for mobile and desktop
- Social media sharing integration (Twitter, LinkedIn, Instagram)
- Download processed images
- Beautiful, modern UI with drag-and-drop support

## Quick Start

### Prerequisites

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd icair-get-dp
   ```

2. **Install dependencies**

   Using `uv` (recommended):

   ```bash
   uv sync
   ```

   Or using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**

   ```bash
   uv run python main.py
   ```

   Or:

   ```bash
   python main.py
   ```

4. **Open in browser**
   Navigate to `http://localhost:8080`

## Customization Guide

This boilerplate is designed to be easily customized for your event or brand. Here's what you need to change:

### 1. Frame Image (`dp.png`)

Replace the `dp.png` file in the root directory with your own frame/template image.

**Requirements:**

- Format: PNG with transparency (RGBA)
- Recommended size: 2000x2000px or larger
- The center area should be transparent (for the user's photo)
- Design your text area where you want the username to appear

### 2. Font File (`fonts/`)

Replace the font file in the `fonts/` directory with your preferred font.

**Supported formats:** `.ttf`, `.otf`

Update the font path in [`main.py`](main.py):

```python
FONT_PATH = os.path.join(os.path.dirname(__file__), "fonts/YourFont.otf")
```

### 3. Python Configuration ([`main.py`](main.py))

Look for `CUSTOMIZATION SECTION` comments in the file. Key settings:

#### **File Paths (Lines 13-20)**

```python
# Replace with your font file path
FONT_PATH = os.path.join(os.path.dirname(__file__), "fonts/ClashDisplay-Medium.otf")

# Replace with your frame/template image path
FRAME_PATH = os.path.join(os.path.dirname(__file__), "dp.png")
```

#### **Layout Configuration (Lines 22-31)**

```python
# Font size as percentage of frame width (0.04 = 4%)
BASE_FONT_SIZE = int(FRAME_WIDTH * 0.04)
```

#### **Image Positioning (Lines 71-87)**

```python
# Circle size as percentage of frame width (0.395 = 39.5%)
circle_diameter = int(FRAME_WIDTH * 0.395)

# Vertical position (0.50 = 50% from top, centered vertically)
paste_y = int(FRAME_HEIGHT * 0.50) - (circle_diameter // 2)
```

#### **Text Positioning (Lines 145-186)**

```python
# Text vertical position (0.745 = 74.5% from top)
text_box_center_y = int(frame_height * 0.745)

# Text color: black (0, 0, 0, 255) - change RGBA values
draw.text((text_x, current_y), line, fill=(0, 0, 0, 255), font=font)
```

### 4. HTML/CSS Configuration ([`templates/index.html`](templates/index.html))

Look for `CUSTOMIZATION` comments in the file:

#### **Page Title (Line 6)**

```html
<title>ICAIR 2025 - Get Your DP</title>
```

#### **Brand Colors (Lines 15-28)**

```css
body {
  background: #5e17eb; /* Primary brand color */
}

h1 {
  color: #5e17eb; /* Primary brand color */
}
```

Search for `#5e17eb` throughout the CSS and replace with your brand color.

#### **Event Information (Lines 541-548)**

```html
<h1 id="pageTitle">ICAIR 2025</h1>
<p class="subtitle" id="pageSubtitle">
  Generate your conference profile picture
</p>
```

#### **Footer Information (Lines 636-641)**

```html
<div class="footer">
  <p>5th International Conference on Artificial Intelligence and Robotics</p>
  <p>November 4-6, 2025 | University of Lagos</p>
</div>
```

#### **Social Media Sharing (Lines 682-684)**

```javascript
const SHARE_TEXT = "Your custom social media message here...";
const SHARE_URL = "https://your-event-website.com/";
```

### 5. Project Metadata ([`pyproject.toml`](pyproject.toml))

Update the project information:

```toml
[project]
name = "your-project-name"
version = "0.1.0"
description = "Your Project Description"
```

## Deployment

### Using Docker

1. Build the image:

   ```bash
   docker build -t dp-generator .
   ```

2. Run the container:
   ```bash
   docker run -p 8080:8080 dp-generator
   ```

### Using Gunicorn (Production)

```bash
gunicorn -w 4 -b 0.0.0.0:8080 main:app
```

### Environment Variables

- `PORT`: Server port (default: 8080)

## File Structure

```bash
.
├── main.py                      # Flask application and image processing logic
├── templates/
│   └── index.html              # Frontend HTML/CSS/JavaScript
├── fonts/
│   └── ClashDisplay-Medium.otf # Custom font (replace with yours)
├── dp.png                      # Frame template image (replace with yours)
├── pyproject.toml              # Project configuration
├── Dockerfile                  # Docker configuration
├── README.md                   # This file
├── CUSTOMIZATION_CHECKLIST.md  # Quick reference checklist
└── LICENSE                     # MIT License
```

## Tips for Best Results

### Frame Design

- Leave the center area transparent for user photos
- Make sure the text area has good contrast
- Test with different image sizes to ensure consistency

### Positioning Values

All positioning uses percentages (0.0 to 1.0) relative to the frame dimensions:

- `0.5` = 50% (center)
- `0.0` = 0% (top/left edge)
- `1.0` = 100% (bottom/right edge)

### Color Formatting

- CSS: Use hex codes (`#5e17eb`)
- Python: Use RGBA tuples (`(94, 23, 235, 255)`)

## Troubleshooting

**Images not loading?**

- Check file paths in `main.py`
- Ensure `dp.png` and font file exist

**Text positioning off?**

- Adjust the percentage values in `add_username_text()` function
- Test with different name lengths

**Colors not matching?**

- Search and replace all instances of the color code in `index.html`
- Update text color in `main.py` if needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to use, modify, and distribute this boilerplate for your own events and projects.

## Credits

Built with Flask, Pillow, and HTML/CSS.
