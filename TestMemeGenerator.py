"""To test main functionality of MemeGenerator module."""

import os
import shutil
from QuoteEngine.QuoteModel import QuoteModel
from MemeGenerator.MemeGenerator import MemeGenerator

jpg_path = './_data/photos/dog/xander_1.jpg'
png_path = './_data/photos/dog/white_dog.png'
path_list = [jpg_path, png_path]
input_path = './_data/photos/dog/xander_1.jpg'


def test_MemeGenerator():
    """Test process."""
    if os.path.exists('./test_dir'):
        shutil.rmtree('./test_dir')

    os.mkdir('./test_dir')
    test_output_dir = './test_dir'
    assert os.path.exists(test_output_dir)

    test_quote_model = QuoteModel(
        body='nothing is everything', author='SChang')

    test_meme_generator = MemeGenerator(test_output_dir)

    assert isinstance(MemeGenerator, test_meme_generator)

    output_path = test_meme_generator.make_meme(
        img_path=input_path,
        text=test_quote_model.body,
        author=test_quote_model.author
    )

    assert os.path.exists(output_path)

    shutil.rmtree(test_output_dir)


if __name__ == '__main__':
    test_MemeGenerator()
