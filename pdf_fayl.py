from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.add_font("DejaVu","","font/DejaVuSansCondensed.ttf",uni=True)
pdf.set_font("DejaVu",size=25)
pdf.cell(200,10,txt="Pythonda yaratildi",ln=1,align="C")
pdf.cell(200,10,txt="Pythonda yaratilgan botga xush kelibsz!",ln=1,align="L")
pdf.output("pdfTest.pdf")