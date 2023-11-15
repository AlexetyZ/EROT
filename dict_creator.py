from Formular_table import get_phrases_list
from direct_pxl import Operation


def create_dict_OT():
    file_path = "C:\\Users\zaitsev_ad\Documents\ЕРОТ\построчные таблицы\\2573 - 1.xlsx"
    operation = Operation(file_path)
    p_q_dict = operation.get_phrase_and_question()
    phrase = p_q_dict[0]
    question = p_q_dict[1]
    dict_ot = get_phrases_list(
        'B',
        'C',
        # 'D',
        # 'E',
        # 'F',
        # 'G',
        # 'H',
        # 'I',
        # 'J',
        # 'K',
        # 'L',
        file_path=file_path,
        phrase_temlpate=phrase,
        question_temlpate=question,
    )
    return dict_ot


def main():
    pass


if __name__ == '__main__':
    main()

