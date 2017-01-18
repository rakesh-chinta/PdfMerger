import PyPDF2

def PDFmerge(pdfs, output):
	pdfMerger = PyPDF2.PdfFileMerger()

	for pdf in pdfs:
		with open(pdf, 'rb') as f:
			pdfMerger.append(f)

	with open(output,'wb') as f:
		pdfMerger.write(f)

def main():
	pdfs = ['example.pdf', 'rotated_example.pdf']

	output = 'combined_example.pdf'

	PDFmerge(pdfs = pdfs, output = output)

if __name__ = "__main__":
	main()