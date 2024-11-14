import sys
import pymupdf


def get_highlights(page):
    # Get all highlights of a page
    # A highlight is defined by 1 or more rectangles
    # A rectangle is defined by 4 coordinates (x,y)

    highlights = []

    for annot in page.annots():

        # https://pymupdf.readthedocs.io/en/latest/vars.html#annotationtypes
        if annot.type[1] == "Highlight":

            # A multi-line highlight will have multiple rectangles
            highlight = []

            # Each rectangle of the highlight is defined by 4 (consecutive) vertices
            for i in range(0, len(annot.vertices), 4):
                highlight.append(pymupdf.Quad(annot.vertices[i:i+4]).rect)

            highlights.append(highlight)

    return highlights


def get_sentences(highlights, words):
    # A (highlighted) sentence is formed when the rectangle of a word
    # intersects with (one of) the rectangle(s) of a highlight

    sentences = []

    for highlight in highlights:

        # 1 sentence can be split in multiple highlight rectangles
        sentence = []
        for highlight_rect in highlight:
            for word in words:
                # A word begins with 4 coordinates, followed by the actual string
                if pymupdf.Rect(word[0:4]).intersects(highlight_rect):
                    sentence.append(word[4])

        sentences.append(" ".join(sentence))

    return sentences


if __name__ == "__main__":
    # Give the path of the pdf in the first argument
    doc = pymupdf.open(sys.argv[1])

    for page in doc:
        sentences = get_sentences(get_highlights(page), page.get_text("words"))

        for sentence in sentences:
            print(sentence)
