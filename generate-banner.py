from pathlib import Path

# To calculate difference between two dates
from datetime import datetime

# To add text on the image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# get current datetime
current = datetime.now()

# Hacktoberfest start datetime
hacktoberfest_start = datetime(2022, 10, 1, 0, 0, 0)

# find days and hours until hacktoberfest starts
days = int((hacktoberfest_start - current).days)
hours = int((hacktoberfest_start - current).total_seconds() -
            days*24*3600) // 3600

# Load banner image
img = Image.open('image/banner.png')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.truetype('font/OpenSans-ExtraBold.ttf', 46)

# Add days and hours to banner image
I1.text((519, 390), str(days), font=myFont, fill=(0, 0, 0))
I1.text((737, 390), str(hours), font=myFont, fill=(0, 0, 0))

# Save the edited image to 'banner' folder
Path("banner").mkdir(parents=True, exist_ok=True)
img.save("banner/banner.png")
