from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel
from typing import List


class IngestorInterface(ABC):
    """
    Abstract interface, to determine if what kind of files could be parsed and parse them.
    It's children class will parse body-author format to QuoteModel object.
    """
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """ to determine if the file type could be parsed
        """
        return path.split('.')[-1] in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        """ to parsed file to list of QuoteModels"""
        pass
