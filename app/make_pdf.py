__doc__ = """Accept some parameter(s) and insert the in a pdf."""

from fpdf import FPDF

def make_pdf(pdf_path, **kwargs):
    """ Create a pdf, with optional text variables."""

    name = kwargs['name']

    pdf = FPDF()

    pdf.add_page()
    pdf.set_font('Arial')
    pdf.set_font_size(18)
    
    pdf.cell(50, 50, 'Hello my name is', 0, 1, 'C')

    pdf.cell(50, 25, name, 0, 1, 'C')

    pdf.output(pdf_path)

