import re

from direct_pxl import Operation
import pymorphy2
import json
from collections import OrderedDict
from Exception_word_cases import exceptions, reg_dict_assistent

"""
Без прерывистости инсоляции в не менее чем в одной комнате 1-3 комнатных квартир, находящихся в северной широте, с 22 апреля по 22 августа продолжительность инсоляции не менее 2,5 ч, с прерывистостью инсоляции - не менее 3 ч.
"""


def get_phrases_list(
        *columns: str,
        file_path: str = '/Users/aleksejzajcev/Desktop/таблица 5.xlsx',
        phrase_temlpate: str,
        question_temlpate: str
):
    dict_to_change = {}
    operation = Operation(wb_path=file_path)
    rows = operation.get_list_from_sh_column(
        *columns,
        start_from_row=3,
    )

    word_to_change_like_in_phrase = re.findall(r'\S+\$\S+', phrase_temlpate)
    word_to_change_like_in_question = re.findall(r'\S+\$\S+', question_temlpate)


    phrases_list = {}
    try:
        for n, row in enumerate(rows):
            print(n)

            if n != 0:
                # print('это первая строчка, где пишутся функциональные фразы')
                # print(f'{row=}')
                formatter_row = []
                for position, cell in enumerate(row):

                    if cell == None:
                        cell = ""

                    if position in dict_to_change:
                        changes = json.loads(dict_to_change[position])

                        for key, value in changes.items():
                            if key == 'case':
                                cell = prepare_for_changes(cell)
                                cell = change_case(cell, value)
                                cell = come_back_changes_for_prepare(cell)



                    formatter_row.append(str(cell))
                row = tuple(formatter_row)

                gender_reformed_phrase_temlpate = reformate_sentense_with_like(
                    word_to_change_like_in_sentence=word_to_change_like_in_phrase,
                    formatter_row=formatter_row,
                    sentence_temlpate=phrase_temlpate,
                )


                gender_reformed_question_temlpate = reformate_sentense_with_like(
                    word_to_change_like_in_sentence=word_to_change_like_in_question,
                    formatter_row=formatter_row,
                    sentence_temlpate=question_temlpate,
                )

                # print(row)
                # print(gender_reformed_phrase_temlpate)
                phrase = formate_sentence(gender_reformed_phrase_temlpate % row)
                question = formate_question(formate_sentence(gender_reformed_question_temlpate % row))

                phrases_list[phrase] = question
            else:
                # print(row)
                for col_num, cells_case in enumerate(row):
                    if cells_case is not None:
                        dict_to_change[col_num] = cells_case
                # print(dict_to_change_case)
        return phrases_list

    except KeyboardInterrupt:
        print("Операция искуссвенно прервана... вот, что успел собрать:")
        return phrases_list


def reformate_sentense_with_like(
        word_to_change_like_in_sentence: list,
        formatter_row: list,
        sentence_temlpate: str,
):
    if word_to_change_like_in_sentence != []:
        for exp in word_to_change_like_in_sentence:
            word = exp.split('$')[0]
            command = exp.split('$')[1]
            reference_number = int(command.split('like')[1])
            reference = formatter_row[reference_number] + ' ' + formatter_row[reference_number+1]
            # print(reference)
            right_gender = gender_like_reference(reference, word)
            new_sentence_temlpate = f'{str(sentence_temlpate).replace(exp, right_gender)}'
            return new_sentence_temlpate
    else:
        return sentence_temlpate


def formate_sentence(sentence):
    sentence = str(sentence).strip()
    sentence = str(sentence).replace("  ", " ").replace("  ", " ").replace("  ", " ")
    sentence = str(sentence).replace(" .", ".").replace(" .", ".")
    sentence = str(sentence).replace(" ?", "?").replace(" ?", "?")

    return sentence


def formate_question(question):

    question = str(question).replace('оваться ', 'уется ')
    question = str(question).replace('оваться,', 'уется,')

    question = str(question).replace('иться ', 'ится ')
    question = str(question).replace('иться,', 'ится,')

    question = str(question).replace('ться ', 'ется ')
    question = str(question).replace('ться,', 'ется,')

    question = str(question).replace('ать ', 'ает ')
    question = str(question).replace('ать,', 'ает,')

    question = str(question).replace(' быть ', ' ')
    question = str(question).replace(' быть,', ', ')

    return question


def prepare_for_changes(string):
    string = str(string).replace(';', ' ;').replace(' ;', ' ; ')
    string = str(string).replace('(', ' (').replace(' (', ' ( ')
    string = str(string).replace(')', ' )').replace(' )', ' ) ')
    string = str(string).replace('-', ' -').replace(' -', ' - ')
    string = str(string).replace('+', ' +')
    string = str(string).replace(',', ' , ')

    return string


def come_back_changes_for_prepare(string):
    string = str(string).replace('  ', ' ')
    string = str(string).replace(' ; ', ';')
    string = str(string).replace(' ( ', '(').replace("( ", "(")
    string = str(string).replace(' ) ', ') ').replace(' )', ')')
    string = str(string).replace(' - ', '-').replace(' -', '-').replace('- ', '-')
    string = str(string).replace(' +', '+')
    string = str(string).replace(' , ', ', ')

    return string


def gender_like_reference(reference, text):
    # print(reference)
    analyser = pymorphy2.MorphAnalyzer()
    parse_text = analyser.parse(text)[0]
    gender = ''
    new_text = text
    split_reference = reference.split()
    for word in split_reference:
        parse_reference = analyser.parse(word)
        # print(word)
        for parse_variants in parse_reference[:1]:
            # print(parse_variants)

            if parse_variants.tag.case == 'nomn' or parse_variants.tag.case == 'accs':

                if parse_variants.tag.number == 'plur':
                    new_text = parse_text.inflect({'plur'})[0]


                else:
                    # print(parse_text.tag.POS)
                    if parse_text.tag.POS == 'ADJS' or parse_text.tag.POS == 'NOUN':
                        gender = parse_variants.tag.gender
                        # print(f'{gender=}')
                        new_text = parse_text.inflect({gender})[0]
                        # return str(new_text)

                    if parse_text.tag.POS == 'VERB':
                        pass

                return str(new_text)



    # print(str(new_text))



def change_case(phrase, case):

    splitphrase = phrase.split()
    # print(splitphrase)
    pma = pymorphy2.MorphAnalyzer()
    changed_phrase = ''
    # print('проходимся по каждому слову')
    changed = False
    for n, sp in enumerate(splitphrase):
        in_reg_ex_dict = reg_dict_assistent(str(sp).lower(), case)
        # обработкка исключений

        if in_reg_ex_dict is not False:
            phrase_part = in_reg_ex_dict

        elif str(sp).lower() in exceptions:
            phrase_part = exceptions[str(sp).lower()][case]

        else:
            # print(f'по слову {sp}')
            parse_sp = pma.parse(sp)
            # print(parse_sp)

            # print('определяем количество варинатов разбора')
            if len(parse_sp) > 1:
                # print('варинатов больше одного')
                found = False
                # print('парсим каждый варинат разбора')
                for n_pars, var in enumerate(parse_sp):

                    # print(f'{var.word=} - {found=}, {changed=}')
                    if changed is not True or found is not True:
                        parse_sp = pma.parse(sp)[0]
                        break

                    if var.tag.POS == 'CONJ':
                        # print("это союс")
                        parse_sp = pma.parse(sp)[0]
                        break
                    if var.tag.case == 'nomn':
                        # print('это существительное')
                        if var.tag.number == 'sing':
                            parse_sp = pma.parse(sp)[n_pars]
                            found = True
                            changed = True
                        else:
                            parse_sp = pma.parse(sp)[n_pars]
                            found = True
                            changed = True
                        break
                    if found is False:
                        parse_sp = pma.parse(sp)[0]
            else:
                # print('варинатов разбора только 1')
                parse_sp = pma.parse(sp)[0]
            if parse_sp.tag.case == 'nomn':

                phrase_part = parse_sp.inflect({case})[0]
                changed = True
            else:
                phrase_part = sp
                changed = False
        if n != 0:
            changed_phrase += ' '
        changed_phrase += phrase_part
    return changed_phrase

    # print(parse_name.inflect({case})[0])


def main():
    reformate_sentense_with_like(
        word_to_change_like_in_sentence=['должен$like0'],
        formatter_row=['уровень воздействия', "гипохлорида-В", "для человека", "0,02 на кг массы тела"],
        sentence_temlpate='%s %s %s не должен$like0 превышать %s'
    )


if __name__ == '__main__':
    main()
