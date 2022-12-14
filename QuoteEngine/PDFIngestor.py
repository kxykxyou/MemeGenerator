"""Parse pdf file to list of QuoteModels."""

from typing import List
import subprocess
import os
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TXTIngestor import TXTIngestor


class PDFIngestor(IngestorInterface):
    """Parse pdf file to list of QuoteModels."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse pdf file to list of QuoteModels."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        if not os.path.exists('./temp'):
            os.mkdir('./temp')

        # use CLI pdftotext to transform the pdf to text file and
        # save it to temp folder
        temp_text_path = './temp/parsed_pdf.txt'
        subprocess.run(['pdftotext', '-layout', path, temp_text_path])
        quote_models = TXTIngestor.parse(temp_text_path)

        # delete the txt file
        os.remove(temp_text_path)

        return quote_models
