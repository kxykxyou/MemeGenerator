"""Abstract class for implement different ingestors."""

from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract interface, to determine if could parse and parse files.

    Its children class will parse body-author format to QuoteModel object.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """To determine if the file type could be parsed."""
        return path.split('.')[-1] in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """To parsed file to list of QuoteModels."""
        pass
