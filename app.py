"""
Web-based meme generator flask app.

Usage:
    Random: randomly create meme images from ./_data/photos, and the quote from
        ./_data/DogQuotes
    Creator: upload your image url, quote and the author's name.
        Only digest png and jpg file type.

FUNCTIONS:
    setup: set up the built-in images and quotes
    meme_rand: render random meme images
    meme_form: render a form page for users to input data
    meme_post: render customized meme images
"""

import random
import os
from flask import Flask, render_template, request
from QuoteEngine.Ingestor import Ingestor
from MemeGenerator.MemeGenerator import FileTypeError, LongTextError
from MemeGenerator.MemeGenerator import UnidentifiedImageError, MemeGenerator
from urllib.error import HTTPError

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """Load all resources to set up built-in data."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    _quotes = sum(
        [Ingestor.parse(quote_file) for quote_file in quote_files],
        [])

    images_path = "./_data/photos"
    _imgs = []

    for root, _, file_names in os.walk(images_path):
        for file_name in file_names:
            if not file_name.startswith('.'):
                _imgs.append(os.path.join(root, file_name))

    return _quotes, _imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # get data from post method
    img_path = request.values['image_url']
    body = request.values['body']
    author = request.values['author']

    if not img_path:
        return render_template('meme_form.html')

    try:
        # Download the target image in the ./temp directory
        path = meme.make_meme(img_path=img_path, text=body, author=author)
        return render_template('meme.html', path=path)

    except (FileTypeError, HTTPError):
        return render_template('InvalidFileType.html')

    except LongTextError:
        return render_template('TooLongText.html')

    except UnidentifiedImageError:
        return render_template('UnidentifiedImage.html')


if __name__ == "__main__":
    app.run()
