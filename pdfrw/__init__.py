# A part of pdfrw (pdfrw.googlecode.com)
# Copyright (C) 2006-2015 Patrick Maupin, Austin, Texas
# MIT license -- See LICENSE.txt for details

from .pdfwriter import PdfWriter
from .pdfreader import PdfReader
from .objects import (PdfObject, PdfName, PdfArray,
                      PdfDict, IndirectPdfDict, PdfString)
from .tokens import PdfTokens
from .errors import PdfParseError

__version__ = '0.2a0'

# Add a tiny bit of compatibility to pyPdf

PdfFileReader = PdfReader
PdfFileWriter = PdfWriter

__all__ = [PdfWriter, PdfReader, PdfObject, PdfName, PdfArray,
           PdfTokens, PdfParseError, PdfDict, IndirectPdfDict,
           PdfString]
