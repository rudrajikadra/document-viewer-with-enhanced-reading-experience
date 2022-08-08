import trafilatura
import sys
import textwrap
import random
from fpdf import FPDF
from trafilatura.settings import use_config


# Converting text extracted from the url to pdf using customised font formatting
def text_to_pdf(text, filename):
	a4_width_mm = 210
	pt_to_mm = 0.35
	fontsize_pt = 10
	fontsize_mm = fontsize_pt * pt_to_mm
	margin_bottom_mm = 10
	character_width_mm = 7 * pt_to_mm
	width_text = a4_width_mm / character_width_mm

	pdf = FPDF(orientation='P', unit='mm', format='A4')
	pdf.set_auto_page_break(True, margin=margin_bottom_mm)
	pdf.add_page()
	pdf.add_font('Arial', '', 'static//fonts//arial.ttf', uni=True)
	pdf.set_font(family='Arial', size=fontsize_pt)
	splitted = text.split('\n')

	for line in splitted:
		lines = textwrap.wrap(line, width_text)

		if len(lines) == 0:
			pdf.ln()

		for wrap in lines:
			pdf.cell(0, fontsize_mm, wrap, ln=1)

	pdf.output(filename, 'F')
	return True


# Extracting context from the url body and scraping only the key components from the website url using trafilatura library 
# and converting that to pdf file using text_to_pdf function
def urlToPDF(url):
	
	try:
		url = str(url)

		config = use_config()
		config.set("DEFAULT", "EXTRACTION_TIMEOUT", "0")

		urlContent = trafilatura.fetch_url(url)

		result = trafilatura.extract(urlContent, config=config, include_comments=False, include_tables=False, no_fallback=True)
		
		try:
			title = str(trafilatura.extract_metadata(urlContent).title).replace(" ", "_").replace("\"", "").replace("\/", "").replace("\\","").replace("'", "")
		except:
			title = "Title " + str(int(random.randint(1,1000)))
		
		title += ".pdf"
		fileNamePDF = "static//pdf//" + title

		checker = text_to_pdf(result, fileNamePDF)
		if checker:
			return str(title)
		else:
			return ""
	except:
		return ""


# urlToPDF("https://www.oracle.com/au/what-is-data-science/")

