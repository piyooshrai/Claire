#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create a 1200x630 image with black background
width = 1200
height = 630
img = Image.new('RGBA', (width, height), color='#0a0a0a')
draw = ImageDraw.Draw(img)

# Try to use a system font, fallback to default
try:
    # Try common system fonts - reduced sizes for better fit
    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
    subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    cta_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
except:
    # Fallback to default font with larger size
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    cta_font = ImageFont.load_default()

# Load the existing logo and resize it
logo_path = "/home/user/Claire/assets/claire-logo.png"
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    # Resize logo to fit nicely (smaller - 300px)
    logo_width = 300
    logo_height = int(logo.height * (logo_width / logo.width))
    logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)

    # Place logo at top center
    logo_x = (width - logo_width) // 2
    logo_y = 50
    img.paste(logo, (logo_x, logo_y), logo)

    # Position text below logo
    text_start_y = logo_y + logo_height + 50
else:
    # If no logo, start text higher
    text_start_y = 150

# Main headline
headline = "Digital Labor That Actually Works"
# Get text bounding box for centering
bbox = draw.textbbox((0, 0), headline, font=title_font)
text_width = bbox[2] - bbox[0]
text_x = (width - text_width) // 2
draw.text((text_x, text_start_y), headline, fill='#ffffff', font=title_font)

# Subtitle - split into two lines for better fit
subtitle_line1 = "AI-Powered Workflows for Healthcare, Legal,"
subtitle_line2 = "Finance & Hospitality"
bbox = draw.textbbox((0, 0), subtitle_line1, font=subtitle_font)
text_width = bbox[2] - bbox[0]
text_x = (width - text_width) // 2
draw.text((text_x, text_start_y + 90), subtitle_line1, fill='#999999', font=subtitle_font)

bbox = draw.textbbox((0, 0), subtitle_line2, font=subtitle_font)
text_width = bbox[2] - bbox[0]
text_x = (width - text_width) // 2
draw.text((text_x, text_start_y + 125), subtitle_line2, fill='#999999', font=subtitle_font)

# Call to action
cta = "Interview Claire for Your Team Today"
bbox = draw.textbbox((0, 0), cta, font=cta_font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
text_x = (width - text_width) // 2
cta_y = height - 120

# Draw CTA box
padding = 18
box_x1 = text_x - padding
box_y1 = cta_y - padding
box_x2 = text_x + text_width + padding
box_y2 = cta_y + text_height + padding
draw.rectangle([box_x1, box_y1, box_x2, box_y2], outline='#ffffff', width=2)
draw.text((text_x, cta_y), cta, fill='#ffffff', font=cta_font)

# Save the image
output_path = "/home/user/Claire/assets/og-image.png"
img.save(output_path, 'PNG')
print(f"Open Graph image created: {output_path}")
print(f"Dimensions: {width}x{height}")
