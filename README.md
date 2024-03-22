# Replace keywords in documents

WARNING: This repo has been done in a hurry, and thus all safety
requirements for develpment are ignored...

## Prerequisities

Install prerequisities:

`python3 -m pip install python-pptx`  
`python3 -m pip install docx`  
`python3 -m pip install doc2docx`  
`python3 -m pip install PyPDF2`  

## Running the script

`python3 --dir [directory_to_process] --docx [--doc --pptx --pdf]`

Real example for MS Word docx files

`python3 --dir "C:/work/doc-replace/data" --docx`

New directory is created fro results: `C:/work/doc-replace/data_N-e-W_`  
Log file is stored in the new directory.

### Configuring the replaced keywords

It is recommended to use the python dictionary.  
Keys shall be unique!  
