"""Ingest csv file of quotes and author names to list of QuoteModels."""


from typing import List
import pandas as pd
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Parse csv file to list of QuoteModels."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse csv file to list of QuoteModels."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        df = pd.read_csv(path, header=0)
        quote_models = []
        for _, row in df.iterrows():
            quote_models.append(QuoteModel(row['body'], row['author']))
        return quote_models
