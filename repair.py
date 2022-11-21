from direct_pxl import Operation
import json
import re
import pymorphy2
from Exception_word_cases import exceptions

def get_phrases_list(
        *columns: str,
        file_path: str = '/Users/aleksejzajcev/Desktop/таблица 5.xlsx',
        phrase_temlpate: str = '%s в %s, находящихся в %s, %s продолжительность инсоляции должна быть не менее %s.',
        question_temlpate: str = '%s в %s, находящихся в %s, %s продолжительность инсоляции не менее %s?'
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
    for n, row in enumerate(rows):

        if n != 0:
            # print(row)
            formatter_row = []
            for position, cell in enumerate(row):

                if cell == None:
                    cell = ""
                if position in dict_to_change:
                    changes = json.loads(dict_to_change[position])

                    for key, value in changes.items():
                        if key == 'case':
                            cell = change_case(cell, value)


                # cell = str(cell).replace(';', '')
                formatter_row.append(cell)
            row = tuple(formatter_row)
            if len(word_to_change_like_in_phrase) > 0:
                for exp in word_to_change_like_in_phrase:
                    word = exp.split('$')[0]
                    command = exp.split('$')[1]
                    reference_number = int(command.split('like')[1])
                    reference = formatter_row[reference_number]
                    new_word = gender_like_reference(reference, word)
                    print(f'{new_word}')
                    phrase_temlpate = phrase_temlpate.replace(exp, new_word)
                    print(f'{phrase_temlpate}')

            if len(word_to_change_like_in_question) > 0:
                for exp in word_to_change_like_in_question:
                    word = exp.split('$')[0]
                    command = exp.split('$')[1]
                    reference_number = int(command.split('like')[1])
                    reference = formatter_row[reference_number]
                    new_word = gender_like_reference(reference, word)
                    print(f'{new_word}')
                    question_temlpate = question_temlpate.replace(exp, new_word)
                    print(f'{question_temlpate}')



            phrases_list[phrase_temlpate % row] = question_temlpate % row
        else:
            # print(row)
            for col_num, cells_case in enumerate(row):
                if cells_case is not None:
                    dict_to_change[col_num] = cells_case
            # print(dict_to_change_case)

    return phrases_list


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


def change_case(phrase, case):
    analyser = pymorphy2.MorphAnalyzer()
    split_phrase = phrase.split()

    for word in split_phrase[:1]:
        all_variants_parse = analyser.parse(word)
        needs_variant_parse = None
        for variant_parse in all_variants_parse:
            variant_case = variant_parse.tag.case
            if variant_case == 'nomn':
                needs_variant_parse = variant_parse
                break
        print(needs_variant_parse)
        # print(analyser.tag(split_phrase[0]))
        # print(analyser.normal_forms(split_phrase[0]))

def analise_sentense(sentense):
    # print(sentense)
    analiser = pymorphy2.MorphAnalyzer()
    _pos: str = ''
    words = sentense.split()
    # print(words)
    for word in words:
        variants_parse = analiser.parse(word)
        real_pos = []
        for variant_parse in variants_parse:
            real_pos.append(variant_parse.tag.POS)
        _pos = f'{_pos} {max(value for value in real_pos)}'
    print(_pos)

def main():
    text = 'Показатель Цисты и ооцисты патогенных кишечных простейших , яйца и личинки гельминтов в горячей воде не определяется .'
    analise_sentense(text)
    # print(change_case(text, 'gent'))
    # file_path = '/Volumes/KINGSTON/построчные таблицы/3 глава табл 3.3 — копия.xlsx'
    # operation = Operation(file_path)
    # p_q_dict = operation.get_phrase_and_question()
    # phrase = p_q_dict[0]
    # question = p_q_dict[1]
    #
    # dict_OT = get_phrases_list(
    #     # 'B',
    #     'C', 'D', 'E', 'F',
    #     # 'G', 'H', 'I',
    #     file_path=file_path,
    #     phrase_temlpate=phrase,
    #     question_temlpate=question
    # )
    #
    # print(f'{len(dict_OT)}\n{dict_OT}')


if __name__ == '__main__':
    main()
