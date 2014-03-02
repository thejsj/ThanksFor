from thanksfor.models import Submission
import StringIO
import random
import os
import settings
from django.core.files.base import ContentFile
from PIL import ImageOps, Image

def cropImage(submission):

    #opening and resizing the thumbnail
    path = os.path.join(settings.MEDIA_ROOT, str(submission.image))
    thumb_file = Image.open(path)

    if thumb_file.mode not in ("L", "RGB"):
        thumb_file = thumb_file.convert("RGB")

    thumb_file.thumbnail((600, 800), Image.ANTIALIAS)
    thumb_file.save(path, "JPEG")