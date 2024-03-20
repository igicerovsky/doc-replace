import re
import argparse
import logging

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import DecodedStreamObject, EncodedStreamObject, NameObject

from config import replace_substring


def replace_text(content, replacements: dict, stat: dict) -> str:
    """ Replace text in a PDF document
        Replacements are case insensitive
        Replacements MUST NOT contain 'BT' or 'ET' or 'TJ' keys
        Returns the modified content
    """
    for k, v in replacements.items():
        content, n = replace_substring(
            content, k, v)
        stat[v] += n

    return content


def process_data(object, replacements, stat: dict):
    data = object.get_data()
    decoded_data = data.decode('utf-8', errors='ignore')

    replaced_data = replace_text(decoded_data, replacements, stat)

    encoded_data = replaced_data.encode('utf-8')
    if object.decoded_self is not None:
        object.decoded_self.set_data(encoded_data)
    else:
        object.set_data(encoded_data)


def replace_pdf(in_path: str, new_path: str, replacements: dict) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True,
                    help="path to PDF document")

    pdf = PdfReader(in_path)
    writer = PdfWriter()

    stat = {value: 0 for value in replacements.values()}
    empty = True

    for page_number in range(0, len(pdf.pages)):
        page = pdf.pages[page_number]
        contents = page.get_contents()

        if contents and (isinstance(contents, DecodedStreamObject) or isinstance(contents, EncodedStreamObject)):
            process_data(contents, replacements, stat)
        elif contents and len(contents) > 0:
            for obj in contents:
                if isinstance(obj, DecodedStreamObject) or isinstance(obj, EncodedStreamObject):
                    streamObj = obj.getObject()
                    process_data(streamObj, replacements, stat)

        # Force content replacement
        if contents and isinstance(page[NameObject("/Contents")], EncodedStreamObject):
            page[NameObject("/Contents")] = contents.decoded_self
            writer.add_page(page)
            empty = False
        else:
            print(f'Page {page_number} text is invalid!')
            logging.info(f'Page {page_number} text is invalid!')

    if empty:
        print(f'No valid pages found in {in_path}')
        logging.error(f'No valid pages found in {in_path}')
        return

    with open(new_path, 'wb') as out_file:
        writer.write(out_file)
    logging.info(f'Replacements:\n  {stat}')
    logging.info(f'New pdf file saved to {new_path}')
