import PyPDF2
import sys
input_PDF = sys.argv[1:]


def pdf_combiner(pdf_lists):
    merged_lists = PyPDF2.PdfFileMerger()
    for file in pdf_lists:
        merged_lists.append(file)
    merged_lists.write('Nam.pdf')


pdf_combiner(input_PDF)
# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page=reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer =PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf','wb') as file2:
#         writer.write(file2)
