import sys
import pymupdf

if __name__ == "__main__":
    # Give the path of the pdf in the first argument
    doc = pymupdf.open(sys.argv[1])

    for page in doc:
        print(page.get_text())
