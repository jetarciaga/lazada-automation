#!/usr/bin/env python3

import PyPDF2
import os

with open('laz_print.pdf', 'rb') as lazada:
    reader = PyPDF2.PdfFileReader(lazada)
    writer = PyPDF2.PdfFileWriter()
    pages = reader.numPages #numPages where page 1 is 0

    for page in range(pages):
        #since 0 is page 1, get even number to get the odd pages
        if page > 1 and page % 2 == 0: #does not include 1st page
            oddpage = reader.getPage(page)
            writer.addPage(oddpage)

    with open('to_print.pdf', 'wb') as docs:
        writer.write(docs)
