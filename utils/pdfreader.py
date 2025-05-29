
import fitz
class Pdfreader():


    def extract_text_pdf(self,file):

        text = ""
        try:
            doc = fitz.open(file)
            for page in doc:
                text += page.get_text()
        except Exception as e:
            text=e

        return text
