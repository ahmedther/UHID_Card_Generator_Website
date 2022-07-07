from reportlab.lib.units import mm
from reportlab.graphics.barcode import code39,code128
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import sys



class GenerateUHIDCard:
    
    
    def __init__(self,filename="Card.pdf", uhid="uhid",patient_name = "patient_name",gender ="gender"):
        """
        @param date: The date to use
        @param amount: The amount owed
        @param receiver: The person who received the amount owed
        """
        # Define Canvas
        self.my_canvas = SimpleDocTemplate(filename, pagesize=(100*mm,54*mm),rightMargin=1, leftMargin=20,topMargin=45,bottomMargin=1)

        # Variable to add in cavanas after collecting data from different source
        flowables = []
        
        # pdfmetrics.registerFont(TTFont("Bookman Old Style Light", "BOOKOS.TTF"))
        # pdfmetrics.registerFont(TTFont("Bookman Old Style Italic", "BBOOKOSI.TTF"))
        # pdfmetrics.registerFont(TTFont("Bookman Old Style Bold Italic", "BOOKOSBI.TTF"))
        # pdfmetrics.registerFont(TTFont("Bookman Old Style Bold", "BOOKOSB.TTF"))
        
        # Defining Fonts
        pdfmetrics.registerFontFamily("Bookman Old Style",normal="Bookman Old Style,",bold="Bookman Old Style Bold", italic="Bookman Old Style Italic", boldItalic="Bookman Old Style Bold Italic" )
        pdfmetrics.registerFont(TTFont('Bookman Old Style','BOOKOSB.TTF'))
        
        # Defining Styles
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='card',
                                  fontName="Bookman Old Style Bold",
                                  fontSize=11,
                                  leading=8))
        styles.add(ParagraphStyle(name ="times",
                                  fontName="Bookman Old Style Bold",
                                  fontSize = 12,
                                  leading = 10))

       # Defining barcode
        bar_code = code128.Code128(uhid,barWidth= 1, barHeight = 20)

        # Adding it all Together
        flowables.append(Paragraph(patient_name,styles["card"]))
        flowables.append(Spacer(1, 8))
        
        flowables.append(Paragraph(gender,styles["card"]))
        flowables.append(Spacer(1, 8))

        flowables.append(Paragraph(uhid,styles["card"]))
        flowables.append(Spacer(1, 18))

        flowables.append(bar_code)
        flowables.append(Spacer(1, 8))


        self.my_canvas.build(flowables)


        #self.my_canvas.drawString(0, 10, data[0])
    
          
        


if __name__ == '__main__':

    GenerateUHIDCard()

    
    # GenLabel('form.pdf', str(ct),
    # '$1,999', 'Mike')
