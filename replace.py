# Description: Replace text in a Word document

from os import getcwd, walk, path
import argparse

from tkinter import filedialog

from config import replace_data, NEW_DOC_SUFFIX
from wordreplace import replace_word
from pdfreplace import replace_pdf


def get_files(directory, exts: tuple) -> list:
    word_files = []
    for root, dirs, files in walk(directory):
        for file in files:
            if file.endswith(exts) and NEW_DOC_SUFFIX not in file:
                word_files.append(path.join(root, file))
    return word_files


def main() -> None:
    """ Main
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dir", help="processing directory", default=None)

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
    try:
        # word_files = get_files(work_dir, ('.doc', '.docx'))
        # for file in word_files:
        #     replace_word(file, rdict)

        pdf_files = get_files(work_dir, ('.pdf'))
        for file in pdf_files:
            replace_pdf(file, rdict)
    except (KeyError, ValueError, FileNotFoundError, ) as e:
        print(e)
        print('Failed!')


if __name__ == "__main__":
    main()
