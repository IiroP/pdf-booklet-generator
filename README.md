# PDF booklet generator

Generate a booklet from PDF (for example "sitsiläsy")

## Requirements
- Python 3.8 or newer
- `pypdf`

## Usage
```
usage: pdfbooklet.py [-h] input output

Create booklet from pdf

positional arguments:
  input       Input PDF file
  output      Output PDF file

options:
  -h, --help  show this help message and exit
```

For example: `python pdfbooklet.py input.pdf output.pdf`