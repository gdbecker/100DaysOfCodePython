# 100 Days of Code: Python
# August 6, 2022
# PDF to audio converter
# Using API to transform text into an audio version

# Import modules
import requests
import PyPDF2
from decouple import config

# Voice RSS API info
api_key = config("api_key")

# Convert the pdf into plain text
pdfFileObj = open("text.pdf", "rb")
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader = PyPDF2.PdfReader(pdfFileObj)
# first_page = pdfReader.getPage(0)
first_page = pdfReader.pages[0]

# text_to_convert = first_page.extractText()
text_to_convert = first_page.extract_text()

pdfFileObj.close()

# API call request info
url = "https://api.voicerss.org/"
source = text_to_convert
language = "en-us"
audio_codecs = "WAV"
parameters = {
    "key": api_key,
    "src": source,
    "hl": language,
    "c": audio_codecs
}

# Convert text to audio
response = requests.get(url=url, params=parameters)
response.raise_for_status()

open("new_audio.mp3", "wb").write(response.content)