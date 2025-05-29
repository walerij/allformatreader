
import fitz
class Pdfreader():


    def extract_text_pdf(self,file):
        doc = fitz.open(file)
        text = ""

        for page in doc:
            text += page.get_text()

        return text
