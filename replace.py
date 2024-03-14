# Description: Replace text in a Word document

from os import getcwd, walk, path
import argparse
import pathlib
import logging

from tkinter import filedialog

from config import replace_data, NEW_DOC_SUFFIX
from wordreplace import replace_word
from pdfreplace import replace_pdf
from pptxreplace import replace_pptx


def get_files(directory, exts: tuple) -> list:
    word_files = []
    for root, dirs, files in walk(directory):
        for file in files:
            if file.endswith(exts) and NEW_DOC_SUFFIX not in file:
                word_files.append(path.join(root, file))
    return word_files


def replace_ext(fn, work_dir, exts: tuple, rdict: dict) -> None:
    """ Replace text in Word documents
    """
    logging.info(f'Looking for files with extension(s): {exts}...')
    files = get_files(work_dir, exts)
    for file in files:
        logging.info(f'\nProcessing {file}...',)
        print(f'\nProcessing {file}...')
        new_file = replace_path(work_dir, file, NEW_DOC_SUFFIX)
        new_dir = pathlib.Path(new_file).parent
        pathlib.Path(new_dir).mkdir(parents=True, exist_ok=True)
        fn(file, new_file, rdict)


def replace_path(work_dir, file, ext: str):
    wp = pathlib.Path(work_dir)
    fl = pathlib.Path(file)
    lst = list(wp.parts)
    lst[-1] = lst[-1] + ext
    wp_new = pathlib.Path(*lst)
    index = fl.parts.index(wp.parts[-1])
    new_path = pathlib.Path(wp_new).joinpath(*fl.parts[index+1:])

    return new_path


def main() -> None:
    """ Main
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dir", help="processing directory", default=None)
    parser.add_argument(
        "--doc", help="Process MS Word (*.doc, *.docx)", action='store_true')
    parser.add_argument(
        "--pdf", help="Process PDF files (*.pdf)", action='store_true')
    parser.add_argument(
        "--ppt", help="Process Power Point files (*.pptx)", action='store_true')

    args = parser.parse_args()
    work_dir = args.dir
    if work_dir:
        work_dir.rstrip("/\\")

    if not work_dir:
        work_dir = filedialog.askdirectory(initialdir=getcwd(),
                                           title="Select a Config Folder")
    if not work_dir:
        print('Work directory not specified or invalid!')
        return

    rdict = replace_data()
    log_path = path.join(getcwd(), 'replace.log')
    logging.basicConfig(filename=log_path,
                        encoding='utf-8', level=logging.DEBUG)
    print(f'Logging to: {log_path}\n')
    logging.info(work_dir)
    try:
        if args.doc:
            replace_ext(replace_word, work_dir, ('.doc', '.docx'), rdict)
        if args.pdf:
            replace_ext(replace_pdf, work_dir, ('.pdf',), rdict)
        if args.ppt:
            replace_ext(replace_pptx, work_dir, ('.pptx'), rdict)
    except (KeyError, ValueError, FileNotFoundError, ) as e:
        logging.info(e)
        logging.info('Failed!')


if __name__ == "__main__":
    main()
