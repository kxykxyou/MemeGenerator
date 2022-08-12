from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TXTIngestor(IngestorInterface):
    """ Parse txt to list of QuoteModels
    """
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        with open(path, 'r') as f:
            quote_models = []
            for line in f.readlines():
                if ' - ' in line:
                    body, author = line.split(
                        ' - ')[0].strip('"'), line.split(' - ')[1].strip('\n')
                    quote_models.append(QuoteModel(body, author))

        return quote_models
