import easyocr

def ocr(img)-> str:
    reader = easyocr.Reader(['fr', 'fr'])
    result = reader.readtext('sms-1.jpg', detail = 0, paragraph=True)
    # return result
    return ' '.join(result)
