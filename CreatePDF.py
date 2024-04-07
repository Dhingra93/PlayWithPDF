from fpdf import FPDF


def createTigerPDF():
    pdf=FPDF(orientation='P',unit='pt',format='A4')  #To set orientation like P or L(Landscape), unit like pt and format of PDF like A4,A%
    pdf.add_page()
    pdf.image('tiger.jpeg',w=80,h=50) #To add page in PDF

    #Following is to add the content in the PDF. FPDF treated as cell and entry is based on cells
    pdf.set_font(family='Times',style='B',size=24)  #The set font should always be on the top of pdf.cell
    pdf.cell(w=0,h=50,txt='Tigers', align='C',ln=1 ) #It take the position of next cell and x=0 ,means the next cell

    pdf.set_font(family='Times',style='B',size=14)
    pdf.cell(w=0,h=15,txt='Description',ln=1)  #ln=1 is to make new line after the cell

    val="""
    The tiger (Panthera tigris) is the largest living cat species and a member of the genus Panthera. It is most recognisable for its black stripes on orange fur with a white underside. An apex predator, it primarily preys on ungulates, such as deer and wild boar. It is territorial and generally a solitary but social predator, requiring large contiguous areas of habitat to support its requirements for prey and rearing of its offspring. Tiger cubs stay with their mother for about two years and then become independent, leaving their mother's territories to establish their own.
    """

    pdf.set_font(family='Times',size=12)
    pdf.multi_cell(w=0,h=15,txt=val) #Multicell doesnot take ln=1 as parameter 

    pdf.set_font(family='Times', size=12)
    pdf.cell(w=100, h=25, txt='Domain:')

    pdf.set_font(family='Times', size=12,style='B')
    pdf.cell(w=100, h=25, txt='Eukaryota',ln=1)

    pdf.set_font(family='Times', size=12)
    pdf.cell(w=100, h=25, txt='Kingdom:')

    pdf.set_font(family='Times', size=12, style='B')
    pdf.cell(w=100, h=25, txt='Animalia')

    pdf.output('1stPDF') #To rename and save PDF output

