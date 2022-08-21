"""Unified interface of four file types ingestor.

Ingestor includes csv, pdf, docx and txt ingestors.
Check the format of four file types in './_data/DogQuotes'
"""

from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor:
    """Provides 4 different file type ingestor.

    Each of Ingestors can ingest data and return a list of QuoteModels.
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

    @classmethod
    def parse(cls, path: str):
        """Parse the file with proper ingestor.

        Args:
            path (str): the path of file which needs to be parsed.
        """
        file_type = path.split('.')[-1]
        parser = cls.ingestors_map.get(file_type.lower())

        return parser.parse(path)
