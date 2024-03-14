# Description: Replace text in a Word document
import logging  # noqa: E402

from docx import Document

from config import NEW_DOC_SUFFIX


def replace_word(doc_path: str, new_path: str, data: dict) -> None:
    """ Replace text in a Word document
    """
    doc = Document(doc_path)

    replaced = {value: 0 for value in data.keys()}
    verbose = False
    for paragraph in doc.paragraphs:
        for key, value in data.items():
            if key in paragraph.text:
                txt_old = paragraph.text
                paragraph.text = paragraph.text.replace(key, value)
                replaced[key] += 1
                print(f'{txt_old} -> {paragraph.text}') if verbose else None

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for key, value in data.items():
                        if key in paragraph.text:
                            txt_old = paragraph.text
                            paragraph.text = paragraph.text.replace(key, value)
                            replaced[key] += 1
                            print(
                                f'{txt_old} -> {paragraph.text}') if verbose else None

    logging.info(f'Replacements:\n  {replaced}')

    doc.save(new_path)
    logging.info(f'New docx file saved to {new_path}')
    print(f'New docx file saved to {new_path}')
