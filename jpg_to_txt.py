from PIL import Image
import pytesseract

def obtain_item_list(image_name):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    text = pytesseract.image_to_string(Image.open(image_name))
    lines = text.splitlines()

    items = []
    for line in lines:
        if len(line) != 0:
            if not line[0].isdigit() and line[-1].isdigit():
                items.append(line)
    item_name = []
    item_price = []
    for item in items:
        name = ""
        data = item.split()
        for i in range (0, len(data)-1):
            name = name + data[i] + " "
        name
        item_price.append(data[-1])
        item_name.append(name)
    return item_name, item_price


item_name, item_price = obtain_item_list('receipt.jpg')
print(item_name)
print(item_price)
