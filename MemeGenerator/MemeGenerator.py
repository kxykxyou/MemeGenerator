from PIL import Image, ImageDraw, ImageFont
import sys
import os
import subprocess
import random
import urllib.request


class MemeGenerator():
    """A meme generator, could combine given text and image together.
    """

    def __init__(self, output_dir: str):
        """output_dir (str): exist directory path. 
            if not exist, will make new directory under current working directory."""
        self.ingested_filetype = [
            'jpg', 'png']  # only work on these file types.

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        self.output_dir = output_dir

    def make_meme(self, img_path: str, text: str, author: str, font_path: str = sys.path[0]+'/fonts/Ubuntu-R.ttf', width=500):
        """load, resize, add text to the image, and save to the output_dir.

        Args:
            img_path (str): Path of image
            font_path (str): Path of font. Defaults to cmb10.
            text (str): Meme text which will be added to the image
            author (str): The meme text author
            width (int, optional): The output image's width. Defaults to 500 and remains ratio. 

        Raises:
            Exception: FileTypeException

        Returns:
            str: output file path
        """

        file_type = img_path.split('.')[-1].lower()
        if file_type not in self.ingested_filetype:
            raise Exception('Only jpg and png files allowed.')

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
        integrated_text = '"' + text + '"' + ' - ' + author
        texted_img.text((random.randint(0, 200), random.randint(0, round(height*4/5))),
                        integrated_text, font=fnt)

        # save processed image
        output_filename = self.output_dir + '/meme_' + \
            img_path.split('/')[-1]
        img.save(output_filename)
        
        if img_path.startswith('http'):
            os.remove(temp_path)
        return output_filename
