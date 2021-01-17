#!/usr/bin/env python3

import PyPDF2
import sys
import os

with open(sys.argv[1], 'rb') as read_file:
    reader = PyPDF2.PdfFileReader(read_file)
    writer = PyPDF2.PdfFileWriter()
    pages = reader.numPages #numPages where first page is 0 not 1

    for page in range(pages):
        #since 0 is page 1, get even number to get the odd pages
        if page > 1 and page % 2 == 0: #does not include 1st page
            oddpage = reader.getPage(page)
            writer.addPage(oddpage)

    with open(sys.argv[2], 'wb') as write_file:
        writer.write(write_file)
