__doc__ = """Accept some parameter(s) and insert the in a pdf."""

from fpdf import FPDF

def create_pdf(pdf_path, **kwargs):
    """ Create a pdf, with optional text variables."""

    name = kwargs['name']

    pdf = FPDF()

    pdf.add_page()
    pdf.set_font('Arial')
    pdf.set_font_size('18')
    
    pdf.cell(50, 50, )



