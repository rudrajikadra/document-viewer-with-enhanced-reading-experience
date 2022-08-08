from PyPDF2 import PdfWriter, PdfReader
import fitz
import sys
from multi_rake import Rake
import random
import math

from PyPDF2.generic import (
    DictionaryObject,
    NumberObject,
    FloatObject,
    NameObject,
    TextStringObject,
    ArrayObject
)


# Create highlight rectangles within the pdf
# x1, y1 starts in bottom left corner
def createHighlight(x1, y1, x2, y2, meta, color = [1, 1, 0]):
    newHighlight = DictionaryObject()

    newHighlight.update({
        NameObject("/F"): NumberObject(4),
        NameObject("/Type"): NameObject("/Annot"),
        NameObject("/Subtype"): NameObject("/Highlight"),

        NameObject("/T"): TextStringObject(meta["author"]),
        NameObject("/Contents"): TextStringObject(meta["contents"]),

        NameObject("/C"): ArrayObject([FloatObject(c) for c in color]),
        NameObject("/Rect"): ArrayObject([
            FloatObject(x1),
            FloatObject(y1),
            FloatObject(x2),
            FloatObject(y2)
        ]),
        NameObject("/QuadPoints"): ArrayObject([
            FloatObject(x1),
            FloatObject(y2),
            FloatObject(x2),
            FloatObject(y2),
            FloatObject(x1),
            FloatObject(y1),
            FloatObject(x2),
            FloatObject(y1)
        ]),
    })

    return newHighlight

def addHighlightToPage(highlight, page, output):
    highlight_ref = output._add_object(highlight)

    if "/Annots" in page:
        page[NameObject("/Annots")].append(highlight_ref)
    else:
        page[NameObject("/Annots")] = ArrayObject([highlight_ref])



# Main function that gets called.
# It accepts the pdf file name and generates its text and using multi_rake it identifies the keywords in the document
# These keywords are then used to highlight in the pdf and save as a new pdf
def highlightOnPDF(file): 

    fileName = "static//pdf//" + str(file)

    pdfInput = PdfReader(open(fileName, "rb"))
    pdfOutput = PdfWriter()
    doc = fitz.open(fileName)

    allText = ""
    for page in pdfInput.pages:
        pageContent = str(page.extract_text())
        allText += str(pageContent)


    rake = Rake()
    keywords = rake.apply(allText)
    updatedKeyWords = [k[0] for k in keywords if k[1]]
    firstVals = math.floor(0.3 * len(updatedKeyWords))
    list_kyes_input = updatedKeyWords[: firstVals]

    for x in range(doc.page_count):
        page1 = pdfInput.getPage(x)
        page = doc.load_page(x)
        extracted = page.get_text("text")
        sentences = extracted.split(".")
        list_input = []
        for j in sentences:
            counter = 0
            for y in list_kyes_input:
                counter += j.count(y)
            if counter >= 3:
                if j.count("\n") <= 3:
                    list_input.append(j[1:])
        for i in list_kyes_input:
            list_input.append(i)

        for y in list_input:
            areas = page.search_for(y)
            pix = page.get_pixmap()
            for i in areas:
                highlight = createHighlight(i[0], pix.height - i[1], i[2], pix.height - i[3], {
                    "author": "",
                    "contents": ""
                })
                addHighlightToPage(highlight, page1, pdfOutput)

        pdfOutput.addPage(page1)

    # Save the newly created pdf with highlights inside the highlighted_pdf folder
    outputFile = "static//highlighted_pdf//" + str(file)
    outputStream = open(outputFile, "wb")
    pdfOutput.write(outputStream)

# highlightOnPDF("Coronavirus.pdf")
