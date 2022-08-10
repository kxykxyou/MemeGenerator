import random
import os
import requests
from flask import Flask, render_template, abort, request
import urllib
from PIL import Image
from QuoteEngine.Ingestor import Ingestor
from MemeGenerator.MemeGenerator import MemeGenerator

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = sum([Ingestor.parse(quote_file)
                 for quote_file in quote_files], [])

    images_path = "./_data/photos"
    imgs = []

    for root, sub_dir, file_names in os.walk(images_path):
        for file_name in file_names:
            if not file_name.startswith('.'):
                imgs.append(os.path.join(root, file_name))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # get data from post method
    img_url = request.values['image_url']
    body = request.values['body']
    author = request.values['author']

    # Download the target image in the ./temp directory
    # Caution: there may be error if the image is ot in {png, jpg}
    img_path = './temp/temp.jpg'
    urllib.request.urlretrieve(img_url, img_path)
    path = meme.make_meme(img_path=img_path, text=body, author=author)

    # remove the temporary saved image.
    os.remove(img_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
