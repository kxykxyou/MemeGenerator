"""A meme generator and error classes.

MemeGenerator instance could set up the output directory.
MemeGenerator.make_meme is main function to open image and
    add meme text on image.
Only jpg and png file are supported to make meme images.

"""

import os
import random
import sys
import textwrap

import urllib.request
from PIL import Image, ImageDraw, ImageFont


class FileTypeError(Exception):
    """To catch wrong file type."""


class LongTextError(Exception):
    """To catch too long text over 150 characters."""


class UnidentifiedImageError(Exception):
    """Can't open via PIL.Image.open() or not a image file."""


class MemeGenerator:
    """A meme generator, could combine given text and image together."""

    def __init__(self, output_dir: str):
        """output_dir (str): exist directory path.

        If not exist, will make new directory under current working directory.
        """
        self.ingested_filetype = [
            'jpg', 'png']  # only work on these file types.

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        self.output_dir = output_dir

    def make_meme(self, img_path: str, text: str, author: str,
                  font_path: str = sys.path[0]+'/fonts/Ubuntu-R.ttf',
                  width=500):
        """Load, resize, add text to the image, and save to the output_dir.

        Args:
            img_path (str): Path of image
            font_path (str): Path of font. Defaults to cmb10.
            text (str): Meme text which will be added to the image
            author (str): The meme text author
            width (int, optional): The output image's width.
            Defaults to 500 and remains ratio.

        Raises:
            Exception: FileTypeException

        Returns:
            str: output file path
        """
        file_type = img_path.split('.')[-1].lower()
        if file_type not in self.ingested_filetype:
            raise FileTypeError('Only jpg and png files allowed.')

        if len(text) + len(author) > 150:
            raise LongTextError('Text or author characters is too long.')

        # load image
        if img_path.startswith('http'):
            temp_path = sys.path[0] + '/temp/' + img_path.split('/')[-1]
            urllib.request.urlretrieve(img_path, temp_path)
            img_path = temp_path

        img = Image.open(img_path)

        # resize image
        ratio = img.width/500
        height = img.height/ratio
        img = img.resize((int(width), int(height)))

        # import fonts with default size=20
        fnt = ImageFont.truetype(font_path, size=20)

        # add text to image
        texted_img = ImageDraw.Draw(img)
        text_location = (random.randint(0, 200),
                         random.randint(0, round(height*4/5)))

        # wrap text in proper width
        integrated_text = textwrap.fill(text, 27) + '\n\n' + '- ' + author
        texted_img.text(text_location, integrated_text, font=fnt)

        # save processed image
        output_filename = self.output_dir + '/meme_' + \
            img_path.split('/')[-1]
        img.save(output_filename)
        if img_path.startswith('http'):
            os.remove(temp_path)

        return output_filename
