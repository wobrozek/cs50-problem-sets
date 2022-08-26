from fpdf import FPDF
import sys

#pip instal fpdf2


"""
using FPDF libary generate pdf like this one https://cs50.harvard.edu/python/2022/psets/8/shirtificate/jharvard.pdf
"""
class PDF(FPDF):
    def header(self):
        self.set_font("helvetica","",40)
        self.cell(0, 10, "CS50 Shirtificate",align="C",new_x="LMARGIN")

    def shirt(self,name):
        self.image("shirtificate.png",0.5,40)
        self.add_font("DejaVuSans",fname="DejaVuSans.ttf")
        self.set_font("DejaVuSans", "", 30)
        self.set_text_color(255, 255, 255)
        self.cell(0,200,f"{name.decode('utf-8')} took CS50", align="C" )

def main():
    name=input("podaj swoję imię i nazwisko: ").encode('utf-8')
    pdf= PDF()
    pdf.add_page()
    pdf.shirt(name)
    pdf.output("shirtificate.pdf")

if __name__=="__main__":
    main()



