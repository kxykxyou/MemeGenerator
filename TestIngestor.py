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
    model = QuoteEngine.QuoteModel('body', 'author')
    return model.body, model.author


def test_CSVIngestor() -> List[QuoteEngine.QuoteModel]:
    quote_models = QuoteEngine.CSVIngestor().parse(csv_simple_lines_path)
    for model in quote_models:
        if type(model) != QuoteEngine.QuoteModel:
            raise Exception('model type != QuoteEngine.QuoteModel')
    return 'CSVIngestor model type test ok'


def test_DOCXIngestor() -> List[QuoteEngine.QuoteModel]:
    quote_models = QuoteEngine.DOCXIngestor().parse(docx_simple_lines_path)
    for model in quote_models:
        if type(model) != QuoteEngine.QuoteModel:
            raise Exception('model type != QuoteEngine.QuoteModel')
    return 'DOCXIngestor model type test ok'


def test_PDFIngestor() -> List[QuoteEngine.QuoteModel]:
    quote_models = QuoteEngine.PDFIngestor().parse(pdf_simple_lines_path)
    for model in quote_models:
        if type(model) != QuoteEngine.QuoteModel:
            raise Exception('model type != QuoteEngine.QuoteModel')
    return 'PDFIngestor model type test ok'


def test_TXTIngestor() -> List[QuoteEngine.QuoteModel]:
    quote_models = QuoteEngine.TXTIngestor().parse(txt_simple_lines_path)
    for model in quote_models:
        if type(model) != QuoteEngine.QuoteModel:
            raise Exception('model type != QuoteEngine.QuoteModel')
    return 'TXTIngestor model type test ok'


def test_Ingestor() -> List[QuoteEngine.QuoteModel]:
    for path in path_list:
        quote_models = QuoteEngine.Ingestor.parse(path)
        for model in quote_models:
            if type(model) != QuoteEngine.QuoteModel:
                raise Exception('model type != QuoteEngine.QuoteModel')
    return 'Ingestor model type test ok'


def test_all():
    assert test_quote_model() == ('body', 'author')
    # assert test_CSVIngestor(
    #     csv_simple_lines_path) == 'CSVIngestor model type test ok'
    assert test_DOCXIngestor() == 'DOCXIngestor model type test ok'
    assert test_PDFIngestor() == 'PDFIngestor model type test ok'
    assert test_TXTIngestor() == 'TXTIngestor model type test ok'
    assert test_Ingestor() == 'Ingestor model type test ok'


if __name__ == '__main__':
    test_all()
