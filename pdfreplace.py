import re
import argparse
import logging

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import DecodedStreamObject, EncodedStreamObject, NameObject

from config import NEW_DOC_SUFFIX


def replace_text(content, replacements: dict, stat: dict) -> str:
    lines = content.splitlines()

    result = ""
    in_text = False

    for line in lines:
        if line == "BT":
            in_text = True

        elif line == "ET":
            in_text = False

        elif in_text:
            cmd = line[-2:]
            if cmd.lower() == 'tj':
                replaced_line = line
                for k, v in replacements.items():
                    if k in replaced_line:
                        res = len(re.findall(f'(?=({k}))', replaced_line))
                        stat[k] += res
                    replaced_line = replaced_line.replace(k, v)
                result += replaced_line + "\n"
            else:
                result += line + "\n"
            continue

        result += line + "\n"

    return result


def process_data(object, replacements, stat: dict):
    data = object.get_data()
    decoded_data = data.decode('utf-8')

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

    stat = {value: 0 for value in replacements.keys()}
    for page_number in range(0, len(pdf.pages)):
        page = pdf.pages[page_number]
        contents = page.get_contents()

        if contents and isinstance(contents, DecodedStreamObject) or isinstance(contents, EncodedStreamObject):
            process_data(contents, replacements, stat)
        elif contents and len(contents) > 0:
            for obj in contents:
                if isinstance(obj, DecodedStreamObject) or isinstance(obj, EncodedStreamObject):
                    streamObj = obj.getObject()
                    process_data(streamObj, replacements, stat)

        # Force content replacement
        if contents and isinstance(page[NameObject("/Contents")], EncodedStreamObject):
            page[NameObject("/Contents")] = contents.decoded_self
        else:
            print(f'Page {page_number} text is invalid!')

        writer.add_page(page)

    with open(new_path, 'wb') as out_file:
        writer.write(out_file)
    logging.info(f'New pdf file saved to {new_path}')

    logging.info(f'Replacements:\n  {stat}')
