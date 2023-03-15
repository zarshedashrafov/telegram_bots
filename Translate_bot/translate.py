from googletrans import Translator

def translate(matn):
    translator=Translator()
    til=translator.detect(matn).lang
    if til=='ar':
        return translator.translate(matn,dest='uz').text
    else:
        return translator.translate(matn,dest='ar').text
