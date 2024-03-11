# Description: Replace text in a Word document

from os import getcwd, walk, path
import argparse
import pathlib

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


def replace_ext(fn, work_dir, exts: tuple, rdict: dict) -> None:
    """ Replace text in Word documents
    """
    files = get_files(work_dir, exts)
    for file in files:
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
    print(work_dir)
    try:
        replace_ext(replace_word, work_dir, ('.doc', '.docx'), rdict)
        replace_ext(replace_pdf, work_dir, ('.pdf',), rdict)
    except (KeyError, ValueError, FileNotFoundError, ) as e:
        print(e)
        print('Failed!')


if __name__ == "__main__":
    main()
