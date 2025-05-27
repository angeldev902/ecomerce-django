import unicodedata
import re

def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    text = text.strip().lower()
    text = re.sub(r'[^\w\s-]', '', text)     # delete special characters
    text = re.sub(r'[\s/]+', '-', text)      # replace blank spaces and "/" by "-"
    return text
