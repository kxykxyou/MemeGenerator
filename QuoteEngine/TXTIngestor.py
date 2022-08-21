"""Parse txt file to list of QuoteModels."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Parse txt to list of QuoteModels."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse txt to list of QuoteModels."""
        if not cls.can_ingest(path):
            raise Exception('can not ingest exception')

        with open(path, 'r') as file:
            quote_models = []
            for line in file.readlines():
                if ' - ' in line:
                    body, author = line.split(
                        ' - ')[0].strip('"'), line.split(' - ')[1].strip('\n')
                    quote_models.append(QuoteModel(body, author))

        return quote_models
