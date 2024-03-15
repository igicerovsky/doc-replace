"""Powerpoint file replace text module"""
import sys  # noqa: E402
import logging  # noqa: E402


from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

from TextReplacer import TextReplacer
from config import replace_substring


def replace_pptx(file_path: str, new_path: str, data: dict) -> None:
    try:
        replacer = TextReplacer(file_path,
                                tables=True,
                                charts=True,
                                textframes=True,
                                slides='',
                                verbose=False,
                                quiet=False)
        replacements = []
        for key, value in data.items():
            replacements.append((key, value))

        # use_regex=True is important for CASEINSENSITIVE matching
        replacer.replace_text(replacements, use_regex=True, verbose=False)
        replacer.write_presentation_to_file(new_path)

    except ValueError as err:
        print(str(err.args[0]), file=sys.stderr)
        logging.error(str(err.args[0]))


def process_shape(shape_parent, data, replaced, verbose=False):
    for shape in shape_parent:
        if shape.has_text_frame:
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    for key, value in data.items():
                        if key in run.text:
                            txt_old = run.text
                            # run.text = run.text.replace(key, value)
                            run.text = replace_substring(
                                run.text, key, value)
                            replaced[key] += 1
                            print(
                                f'{txt_old} -> {run.text}') if verbose else None

        if shape.has_table:
            table = shape.table
            for cell in table.iter_cells():
                # here you can access the text in cell by using
                # cell.text
                # just remember that the shape object refers to the table in this context not the cell
                for key, value in data.items():
                    if key in cell.text:
                        txt_old = cell.text
                        # cell.text = cell.text.replace(key, value)
                        cell.text = replace_substring(
                            cell.text, key, value)
                        replaced[key] += 1
                        print(
                            f'{txt_old} -> {cell.text}') if verbose else None

        if shape.has_notes_slide:
            notes_slide = shape.notes_slide
            for key, value in data.items():
                if key in notes_slide.notes_text_frame.text:
                    txt_old = notes_slide.notes_text_frame.text
                    # notes_slide.notes_text_frame.text = notes_slide.notes_text_frame.text.replace(
                    #     key, value)
                    notes_slide.notes_text_frame.text = replace_substring(
                        notes_slide.notes_text_frame.text, key, value)
                    replaced[key] += 1
                    print(
                        f'{txt_old} -> {notes_slide.notes_text_frame.text}') if verbose else None

        if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
            process_shapes(shape, data, replaced, verbose)


def replace_pptx_old(file_path: str, new_path: str, data: dict) -> None:
    prs = Presentation(file_path)

    # text_runs will be populated with a list of strings,
    # one for each text run in presentation
    replaced = {value: 0 for value in data.keys()}
    verbose = False
    for slide in prs.slides:
        process_shape(slide, data, replaced, verbose)

    logging.info(f'Replacements:\n  {replaced}')

    prs.save(new_path)
    logging.info(f'New PPTX file saved to {new_path}')
