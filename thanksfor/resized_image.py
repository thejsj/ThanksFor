from imagekit import ImageSpec
from imagekit.processors import ResizeToFill, Transpose

class ResizedImage(ImageSpec):
    processors=[
    	Transpose(),
    	ResizeToFill(600, 800),
    ],
    format='JPEG',
    options={'quality': 60}