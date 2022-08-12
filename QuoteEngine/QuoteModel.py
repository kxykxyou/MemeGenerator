class QuoteModel:
    """ to hold quote text(body) and author infos
    """

    def __init__(self, body: str, author: str):
        """ 
        Args:
            body (str): quote text
            author (str): author name
        """
        self.body = body
        self.author = author
