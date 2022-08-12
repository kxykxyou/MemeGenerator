from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import docx


class DOCXIngestor(IngestorInterface):
    """ Parse docx to list of QuoteModels
    """
    allowed_extensions = ['docx', 'doc']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quote_models = []
        doc = docx.Document(path)
        for line in doc.paragraphs:
            if ' - ' in line.text:
                body = line.text.split(' - ')[0].strip('"')
                author = line.text.split(' - ')[1]
                quote_models.append(QuoteModel(body, author))

        return quote_models
