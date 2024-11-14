# Pdf Extract highlights

A script using [PyMuPdf](https://github.com/pymupdf/PyMuPDF) to extract the highlighted text from a pdf.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
# or
pip install pymupdf
```

## Usage

```bash
python extract-highlights.py sample.pdf
# Redirect to .txt file:
python extract-highlights.py sample.pdf > filename.txt
```
