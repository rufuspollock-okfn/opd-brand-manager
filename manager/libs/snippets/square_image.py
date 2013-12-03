from PIL import Image
from django.core.files.storage import default_storage as storage


def square_image(filename, size, format='jpeg'):
    """
    Transform an image located in the default storage at filename
    to the given square size.
    """

    if storage.exists(filename):
        try:
            image = Image.open(storage.open(filename))
            image.thumbnail(size, Image.ANTIALIAS)
            final_image = Image.new("RGB", size, "white")
            final_image.paste(image, (
                (size[0] - image.size[0]) / 2,
                (size[1] - image.size[1]) / 2))
            fd = storage.open(filename, 'w')
            final_image.save(fd, format)
            fd.close()
        except IOError as e:
            raise IOError(
                "The image you submitted can't be read. "
                "Please check its format. (%s)" % e.strerror)
