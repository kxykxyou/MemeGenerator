"""Class model for quotes."""


class QuoteModel:
    """To hold quote text(body) and author infos."""

    def __init__(self, body: str, author: str):
        """Initialize quote model.

        Args:
            body (str): quote text
            author (str): author name
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Represent a quote."""
        return f'{self.body} - {self.author}'
