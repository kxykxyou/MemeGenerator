from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas as pd


class CSVIngestor(IngestorInterface):
    """ Parse csv to list of QuoteModels
    """
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('connot ingest exception')

        df = pd.read_csv(path, header=0)
        quote_models = []
        for idx, row in df.iterrows():
            quote_models.append(QuoteModel(row['body'], row['author']))
        return quote_models


if __name__ == '__main__':
    CSVIngestor().parse()
