from Formular_table import get_phrases_list
from direct_pxl import Operation
from dict_creator import create_dict_OT
import json


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

def main():
    test_table_phrases()
    # count_dolg()
    #  %s, в перио ды начала купального сезона, максимальной антропотехногенной нагрузки.


if __name__ == '__main__':
    main()
