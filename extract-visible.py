import sys
import pymupdf

if __name__ == "__main__":
    # Give the path of the pdf in the first argument
    doc = pymupdf.open(sys.argv[1])
    
    for page in doc:

        tp = page.get_textpage()
        d = tp.extractDICT(sort=True)
        
        text = []
        for block in d['blocks']:
            for line in block['lines']:
                for span in line['spans']:

                    # filter all text that is not white
                    if span['color'] != 0xffffff: 
                        text.append(span['text'])
                    else:
                        text.append('\n\n')

        print(''.join(text))
