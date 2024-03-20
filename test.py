from Formular_table import get_phrases_list
from direct_pxl import Operation
from dict_creator import create_dict_OT
import json
import openpyxl
from pprint import pprint


def test_table_phrases():
    dict_OT = create_dict_OT()
    print(f'\nв кортеже {len(dict_OT)} записей:\n')
    for n, (phrase, question) in enumerate(dict_OT.items()):
        print('')
        print(f'{n+1}. \n{phrase}')
        print(question)
        print('')


def count_dolg():
    with open('/Users/aleksejzajcev/PycharmProjects/EROT/долги_name.json', 'r') as f:
        dolg = json.load(f)

    print(len(dolg))


def form_ot_from_file(filePath):
    wb = openpyxl.load_workbook(filePath)
    sh = wb.worksheets[0]
    SEs = []
    currentSE = None
    currentOTs = []
    for row in sh.iter_rows(min_col=2, max_col=4, min_row=2, values_only=True):
        print(row)
        if row[0]:
            if currentSE:
                SEs.append({
                    'seId': currentSE,
                    'ots': currentOTs
                })
            currentSE = row[0]
            currentOTs = []
        currentOTs.append(
            {
                'title': row[1],
                'checkQuestion': row[2],
            }
        )
    else:
        SEs.append({
            'seId': currentSE,
            'ots': currentOTs
        })







def main():
    filePath = "C:\\Users\zaitsev_ad\Desktop\ОТ.xlsx"
    form_ot_from_file(filePath)
    # count_dolg()
    #  %s, в перио ды начала купального сезона, максимальной антропотехногенной нагрузки.


if __name__ == '__main__':
    main()
