from PIL import Image


def load_image(image_file):
    """
    Load uploaded image.
    """
    return Image.open(image_file)