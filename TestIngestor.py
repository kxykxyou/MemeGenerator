"""To test main functionality of Ingestor module."""

import QuoteEngine
from typing import List

csv_simple_lines_path = './_data/SimpleLines/SimpleLines.csv'
docx_simple_lines_path = './_data/SimpleLines/SimpleLines.docx'
pdf_simple_lines_path = './_data/SimpleLines/SimpleLines.pdf'
txt_simple_lines_path = './_data/SimpleLines/SimpleLines.txt'
path_list = [
    csv_simple_lines_path,
    docx_simple_lines_path,
    pdf_simple_lines_path,
    txt_simple_lines_path,
]


def test_quote_model():
    """Test QuoteModel module."""
    model = QuoteEngine.QuoteModel('body', 'author')
    return model.body, model.author


def test_CSVIngestor() -> List[QuoteEngine.QuoteModel]:
    """Test CSVIngestor module."""
    quote_models = QuoteEngine.CSVIngestor().parse(csv_simple_lines_path)
    for model in quote_models:
        if type(model) != QuoteEngine.QuoteModel:
            raise Exception('model type != QuoteEngine.QuoteModel')
    return True


def test_DOCXIngestor() -> List[QuoteEngine.QuoteModel]:
    """Test DOCXIngestor module."""
    quote_models = QuoteEngine.DOCXIngestor().parse(docx_simple_lines_path)
    for model in quote_models:
        if type(model) != QuoteEngine.QuoteModel:
            raise Exception('model type != QuoteEngine.QuoteModel')
    return True


def test_PDFIngestor() -> List[QuoteEngine.QuoteModel]:
    """Test PDFIngestor module."""
    quote_models = QuoteEngine.PDFIngestor().parse(pdf_simple_lines_path)
    for model in quote_models:
        if type(model) != QuoteEngine.QuoteModel:
            raise Exception('model type != QuoteEngine.QuoteModel')
    return True


def test_TXTIngestor() -> List[QuoteEngine.QuoteModel]:
    """Test TXTIngestor module."""
    quote_models = QuoteEngine.TXTIngestor().parse(txt_simple_lines_path)
    for model in quote_models:
        if type(model) != QuoteEngine.QuoteModel:
            raise Exception('model type != QuoteEngine.QuoteModel')
    return True


def test_Ingestor() -> List[QuoteEngine.QuoteModel]:
    """Test Ingestor module."""
    for path in path_list:
        quote_models = QuoteEngine.Ingestor.parse(path)
        for model in quote_models:
            if type(model) != QuoteEngine.QuoteModel:
                raise Exception('model type != QuoteEngine.QuoteModel')
    return True


def test_all():
    """Test all functions above."""
    assert test_quote_model()
    assert test_CSVIngestor()
    assert test_DOCXIngestor()
    assert test_PDFIngestor()
    assert test_TXTIngestor()
    assert test_Ingestor()


if __name__ == '__main__':
    test_all()
