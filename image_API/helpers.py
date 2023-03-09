from pathlib import Path
from PIL import Image as pillow
from django.core.files import File
from .models import Thumbnail


def thumbnail(base_image, size):
    path = Path(base_image.image.path)

    img = pillow.open(path)
    img.thumbnail((size, size))
    img_path = path.parent / f'{path.stem}_{size}px{path.suffix}'
    img.save(img_path)
    with open(img_path, 'rb') as f:
        Thumbnail.objects.create(
            original=base_image,
            image=File(f),
            size=size
        )
    img_path.unlink()
