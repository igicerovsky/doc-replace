"""Powerpoint file replace text module"""
import logging  # noqa: E402

from pptx import Presentation

from pptx import Presentation


def replace_pptx(file_path: str, new_path: str, data: dict) -> None:
    prs = Presentation(file_path)

    # text_runs will be populated with a list of strings,
    # one for each text run in presentation
    replaced = {value: 0 for value in data.keys()}
    verbose = False
    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    for key, value in data.items():
                        if key in run.text:
                            txt_old = run.text
                            run.text = run.text.replace(key, value)
                            replaced[key] += 1
                            print(
                                f'{txt_old} -> {run.text}') if verbose else None

    for slide in prs.slides:
        for shape in slide.shapes:
            if shape.has_table:
                table = shape.table
                for cell in table.iter_cells():
                    # here you can access the text in cell by using
                    # cell.text
                    # just remember that the shape object refers to the table in this context not the cell
                    for key, value in data.items():
                        if key in cell.text:
                            txt_old = cell.text
                            cell.text = cell.text.replace(key, value)
                            replaced[key] += 1
                            print(
                                f'{txt_old} -> {cell.text}') if verbose else None

    for slide in prs.slides:
        if not slide.has_notes_slide:
            continue
        notes_slide = slide.notes_slide
        for key, value in data.items():
            if key in notes_slide.notes_text_frame.text:
                txt_old = notes_slide.notes_text_frame.text
                notes_slide.notes_text_frame.text = notes_slide.notes_text_frame.text.replace(
                    key, value)
                replaced[key] += 1
                print(
                    f'{txt_old} -> {notes_slide.notes_text_frame.text}') if verbose else None

    logging.info(f'Replacements:\n  {replaced}')

    prs.save(new_path)
    logging.info(f'New PPTX file saved to {new_path}')
