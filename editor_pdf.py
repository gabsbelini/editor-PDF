import PyPDF2
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import sys


'''can.drawString(4920, 800) Posiciona prar escrita no número do pedido.'''


packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
#Posicao de escrita do argumento e o argumento passado por command line: can.drawString(posIni, posFim, sys.argv[1])
#can.drawString(300, 115, "Hello world")
can.setFont("Helvetica", 50)
can.drawString(4920, 800, "")
can.save()
#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PyPDF2.PdfFileReader(packet)
# read your existing PDF
existing_pdf = PyPDF2.PdfFileReader(open("original.pdf", "rb"))
num_pages = existing_pdf.numPages # pega numero de paginas do pdf original
output = PyPDF2.PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(num_pages-1) # pega a ultima pagina do pdf original
page.mergePage(new_pdf.getPage(0)) # junta ultima pagina do pdf original com a "primeira" pagina do pdf criado
x = existing_pdf.getNumPages()
#add all pages from original pdf into output pdf
for n in range(x):
    output.addPage(existing_pdf.getPage(n))
# finally, write "output" to a real file
outputStream = open("arquivo.pdf", "wb")
output.write(outputStream)
outputStream.close()
