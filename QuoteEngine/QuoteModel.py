class QuoteModel:
    """
    Basic quote model class including:

    body: str
    author: str
    """

    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author
