import os
import sys
import random
from QuoteEngine.Ingestor import Ingestor, QuoteModel
from MemeGenerator.MemeGenerator import MemeGenerator


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images_dirs = sys.path[0]+"/_data/photos/"
        imgs = []
        for root, dirs, files in os.walk(images_dirs):
            imgs.extend([os.path.join(root, name) for name in files])

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = [sys.path[0]+'/_data/DogQuotes/DogQuotesTXT.txt',
                       sys.path[0]+'/_data/DogQuotes/DogQuotesDOCX.docx',
                       sys.path[0]+'/_data/DogQuotes/DogQuotesPDF.pdf',
                       sys.path[0]+'/_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeGenerator(sys.path[0]+'/CLIOutput')

    output_path = meme.make_meme(img, quote.body, quote.author)
    print(f'New meme image is generated and save here: ')

    return output_path


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    # optional arguments; if equals none, will be randomly choose from _data
    # -path - path to an image file
    # -body - quote body to add to the image
    # -author - quote author to add to the image
    parser.add_argument('-path', help='Image path', type=str)
    parser.add_argument('-body', help='The meme sentence', type=str)
    parser.add_argument('-author', help='the author of the sentence', type=str)
    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
