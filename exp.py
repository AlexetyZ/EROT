from Formular_table import get_phrases_list, change_case
from direct_pxl import Operation
import pymorphy2
from Exception_word_cases import exceptions
import re

# phrase = 'возбудители кишечных инфекций вирусной природы'
# print(change_case(phrase, 'gent'))


def gender_like_reference(reference, text):
    analyser = pymorphy2.MorphAnalyzer()
    parse_text = analyser.parse(text)[0]
    gender = ''
    new_text = text
    split_reference = reference.split()
    for word in split_reference:
        parse_reference = analyser.parse(word)
        for parse_variants in parse_reference:

            if parse_variants.tag.case == 'nomn':

                if parse_variants.tag.number == 'plur':
                    new_text = parse_text.inflect({'plur'})[0]

                else:
                    print(parse_text.tag.POS)
                    if parse_text.tag.POS == 'ADJS':
                        gender = parse_variants.tag.gender
                        new_text = parse_text.inflect({gender})[0]
                        break
                    if parse_text.tag.POS == 'VERB':
                        pass

    return new_text

def srting_func():
    string = 'АлкенилС12-С14амины'
    string = change_case(string, 'gent')
    return string


def except_words():
    sentence_temlpate = '%s %s %s не должен$like0 превышать %s'
    sentence_temlpate = sentence_temlpate.replace('должен$like0', 'должна')
    print(sentence_temlpate)


def plusing_spisoks():
    spisok_2 = [4, 5, 6]
    spisok_1 = [1, 2, 3, *spisok_2]

    i = 4
    if i in spisok_2:
        print('in sp2')

    if i in spisok_1:
        print('in sp1')


    print(spisok_1)

def reg_ex_dict():
    re_dict = {
        r'ция$': {
            'gent': 'цию',
            'datv': '',
            'accs': '',
            'ablt': '',
            'loct': '',
        }
    }

    def reg_dict_assistent(w, case=None) -> str or bool:
        """
        :param w: опытное слово - слово, испытывается на наличие его окончания (регулярным выражением) в словаре регулярных
        выражений. С целью найти подходящее окончание. ТОЛЬКО ОКОНЧАНИЕ, БЛЯДЬ, А НЕ ЧАСТИ СЛОВА В СЕРЕДИНЕ!!! НЕ ЗАБУДЬ ОПЯТЬ!!!
        :param case: Падеж, на который следует изменить опытное слово, от него зависит подбираемое окончание.
        :return: Опытное слово в установленном падеже, при отсутстии параметра case вернутся буловое значение в зависимости от наличия окончания в словаре
        """
        for key, value in re_dict.items():
            searching = re.search(key, w)
            if searching:
                if case is None:
                    return True
                return searching.string[:searching.start()] + value[case]   # соединяет первые символы опытного слова за исключением искомого выражения и соединяет с соответствующим выражением в зависимости от падежа
        return False




    word = 'крыша'
    print(reg_dict_assistent(word))



def main():
    reg_ex_dict()
    # plusing_spisoks()
    # except_words()

    # print(srting_func())
    # reference = 'общие минерализации'
    # text = 'соответствует'
    # print(gender_like_reference(reference, text))


if __name__ == '__main__':
    main()

