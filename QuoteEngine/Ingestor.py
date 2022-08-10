from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor
from typing import List


class Ingestor:
    """
    Ingrester provides 4 different file type ingestor,
        each of them can ingest data and return a list of QouteModels.
    Ingestor interface which can inherit from ingestors as below:
    1. CSVIngestor
    2. DOCXIngestor
    3. PDFIngestor
    4. TXTIngestor
    """

    ingestors_map = {
        'csv': CSVIngestor,
        'docx': DOCXIngestor,
        'pdf': PDFIngestor,
        'txt': TXTIngestor,
    }

    def __init__(self):
        pass

    @classmethod
    def parse(cls, path: str):
        """ parse the file with proper ingestor

        Args:
            path (str): the path of file which needs to be parsed.
        """
        file_type = path.split('.')[-1]
        parser = cls.ingestors_map.get(file_type.lower())

        return parser.parse(path)
