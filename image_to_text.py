import easyocr

def recognize_form(file_path):
    reader = easyocr.Reader(['ru', 'en'])
    result = reader.recognize(file_path, detail=0, )
    return result

def main():
    file_path = '/Users/aleksejzajcev/Desktop/Снимок экрана 2022-10-13 в 20.03.12.png'
    print(recognize_form(file_path))


if __name__ == '__main__':
    main()
