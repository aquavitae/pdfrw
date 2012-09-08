# A part of pdfrw (pdfrw.googlecode.com)
# Copyright (C) 2006-2009 Patrick Maupin, Austin, Texas
# MIT license -- See LICENSE.txt for details

from pdfrw.pdfwriter import PdfWriter
from pdfrw.pdfreader import PdfReader
from pdfrw.objects import PdfObject, PdfName, PdfArray, PdfDict, IndirectPdfDict, PdfString
from pdfrw.tokens import PdfTokens
from pdfrw.errors import PdfParseError

# Add a tiny bit of compatibility to pyPdf

PdfFileReader = PdfReader
PdfFileWriter = PdfWriter
