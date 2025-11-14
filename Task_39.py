
from pypdf import PdfReader
from gtts import gTTS

reader = PdfReader("operators_task.pdf")
# Open a text file to write the extracted content
txt_file = ''
for page in reader.pages:
    text = page.extract_text()
    if text:  # check if page has text
        txt_file += text +"\n"

tts_pdf = gTTS(txt_file,lang='en')
tts_pdf.save('pdf_audio.mp3')
