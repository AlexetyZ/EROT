import xmltodict
import openpyxl
from datetime import datetime
from tqdm import tqdm
import os

_list_attr = ["STATUS", "STATUS_DATE", "NUMB_DOC", "SERIALNUMB", "BLANKVER", "DATE_DOC", "NAME_PROD", "FIRMMADE_NAME",
              "FIRMGET_NAME", "DOC_NORM", "DOC_PROTOCOL", "WHO", "DOC_USEAREA"]

DIRPATH = "C:\\Users\zaitsev_ad\Downloads"


def main():
    print(f'{datetime.now()} - начало операции')
    with open(os.path.join(DIRPATH, "Registry_2024-03-13.xml"), 'r', encoding="utf8") as myfile:
        sgrs = xmltodict.parse(myfile.read())
    wb = openpyxl.Workbook()
    sh = wb.worksheets[0]
    sh.append(_list_attr)
    for sgr in tqdm(sgrs['ROOT']['DOCUMENT'], desc='собираем значения...'):
        row = []
        for attr in _list_attr:
            if attr in sgr:
                row.append(sgr[attr])
            else:
                row.append('отсутствует (код 007)')
        sh.append(row)
    print(f'{datetime.now()} - сохранение файла')
    wb.save(os.path.join(DIRPATH, 'выгрузка СГР.xlsx'))
    print(f'{datetime.now()} - завершено')


if __name__ == '__main__':
    main()
