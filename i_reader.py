from dataclasses import dataclass

import pymorphy2

punctuation = ['.', ',', ':', '(', ')', ':']
joiners = ['и', 'или', 'либо']

not_caseble = ['PREP', 'PRCL', 'VERB', *punctuation, *joiners]


@dataclass
class ModelWord:
    POS: str
    case: str = 'not_caseble'
    word: str = 'word'

    def __str__(self):
        return self.case


class TextAnaliser:
    def __init__(self):
        self.analiser = pymorphy2.MorphAnalyzer()

    def prepare_for_analise(self, sentense: str):
        for punt in punctuation:
            sentense = sentense.replace(str(punt), " " + str(punt) + " ")

        return sentense

    def get_pos_list(self, sentense: str) -> list:
        sentense = self.prepare_for_analise(sentense)
        words = sentense.split()
        _pos: list = []
        for word in words:
            needs_variant_parse = None
            variants_parse = self.analiser.parse(word)
            real_pos = []
            real_case = []
            for variant_parse in variants_parse:
                real_pos.append(variant_parse.tag.POS)
            probable_pos = str(max(value for value in real_pos))

            if probable_pos not in not_caseble and word not in not_caseble:
                print(f'{word} {probable_pos}')
                for variant_parse in variants_parse:

                    real_case.append(variant_parse.tag.case)
                probable_case = str(max(value for value in real_case if value is not None))
            else:
                probable_case = 'not_cassable'

            _pos.append(ModelWord(POS=probable_pos, word=word, case=probable_case))
        return _pos

    def get_str_from_pos_list(self, _pos) -> str:
        string = ''
        for model_word in _pos:
            # print(_pos.index(model_word))
            if model_word.word in punctuation:
                string = string + " " + model_word.word

            else:
                string = string + " " + model_word.__str__()
        return string

    def parse_word(self, word: str, case: str = 'nomn'):
        parse_list = self.analiser.parse(word)
        nedeed_case = []
        for parse in parse_list:
            if parse.tag.case == case:
                nedeed_case.append(parse)
        return nedeed_case

    def esense(self, _pos):
        what = ModelWord
        for word in _pos:
            if word.POS == 'NOUN':
                what = word
                break
        return f'речь про {what.word}'




if __name__ == '__main__':
    analiser = TextAnaliser()

    text = 'Содержание в воде взвешенных веществ неприродного происхождения (хлопья гидроксидов металлов, образующихся при обработке сточных вод, частички асбеста, стекловолокна, базальта, капрона, лавсана) не допускается'
    result = analiser.get_pos_list(text)
    print(analiser.get_str_from_pos_list(result))
    print(analiser.esense(result))

    # result = analiser.parse_word('аромата', 'nomn')
    # print(result)
