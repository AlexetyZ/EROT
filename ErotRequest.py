import requests
from config import Zaitsev_knd
from crypto import Crypto
from pprint import pprint
import json
import openpyxl


class Erot:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            # 'Authority': 'rg.gov.ru',
            # 'Method': 'POST',
            # 'Accept': 'application/json, text/plain, */*',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # "Accept-Language": "ru,en;q=0.9",
            # "Cache-Control": "no-cache",
            # "Expires": "Sat, 01 Jan 2000 00:00:00 GMT",
            # "If-Modified-Since": "0",
            # "Pragma": "no-cache",
            # "Sec-Fetch-Dest": "empty",
            # "Sec-Fetch-Mode": "cors",
            # "Sec-Fetch-Site": "same-origin",
            'Content-Type': 'application/json',
            'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.4.999 (corp) Yowser/2.5 Safari/537.36",
        }
        self.autorize()

    def autorize(self):
        body = {
            'identifier': Zaitsev_knd['login'],
            'password': Crypto().unpack_password(Zaitsev_knd['password'])
        }
        r = self.session.post(url="https://rg.gov.ru/mzi/auth/signIn", json=body, headers=self.headers)
        print(r)

    def add_se(self, npaId, text, formData):
        json_data = {
            'recommendationType': 'Mandatory',
            'source': 'Manual',
            'state': 'Accepted',
            'color': 'Default',
            'partialIntersectedIds': [],
            'content': text,
            'formData': formData
            # 'formData': {
            #     'section': None,
            #     'subsection': None,
            #     'chapter': None,
            #     'article': '17',
            #     'item': None,
            #     'subitem': None,
            #     'indent': None,
            #     'other': 'часть 5',
            # },
        }
        se = requests.post(
            f'https://rg.gov.ru/api/npaKnds/{npaId}/mrrecommendations/add',
            headers=self.headers,
            json=json_data,
        ).content
        print(se)
        return se['id']

    def add_ot(self, seId, ots):
        # ots it's a list ot like {'checkQuestion': checkQuestion, 'title': title}
        body = {'mrBlocks': [{'additionalInfo': {'costEstimationFiles': [],
                                  'documentReleaseFOIV': [],
                                  'documentReleaseFOIVOther': None,
                                  'files': None},
                                'commonInfo': {'activitySubtype': ['00', '39', '86'],
                                          'assessmentForm': ['AssessmentForm_01'],
                                          'categoriesOfPersons': ['CategoryOfPersons_04',
                                                                  'CategoryOfPersons_01',
                                                                  'CategoryOfPersons_02',
                                                                  'CategoryOfPersons_03'],
                                          'categoriesOfPersonsOtherTitle': None,
                                          'interestedFOIV': ['OIV_00064'],
                                          'publicRelationSpheres': ['PublicRelationSpheres_00024',
                                                                    'PublicRelationSpheres_00023',
                                                                    'PublicRelationSpheres_00011',
                                                                    'PublicRelationSpheres_00017',
                                                                    'PublicRelationSpheres_00013',
                                                                    'PublicRelationSpheres_00003',
                                                                    'PublicRelationSpheres_00004',
                                                                    'PublicRelationSpheres_00001',
                                                                    'PublicRelationSpheres_00002',
                                                                    'PublicRelationSpheres_00030',
                                                                    'PublicRelationSpheres_00027',
                                                                    'PublicRelationSpheres_00038',
                                                                    'PublicRelationSpheres_00046',
                                                                    'PublicRelationSpheres_00025',
                                                                    'PublicRelationSpheres_00026',
                                                                    'PublicRelationSpheres_00077',
                                                                    'PublicRelationSpheres_00053',
                                                                    'PublicRelationSpheres_00018',
                                                                    'PublicRelationSpheres_00009',
                                                                    'PublicRelationSpheres_00008',
                                                                    'PublicRelationSpheres_00010']},
                                'controlTypeId': 'GovernmentControlKind_00002',
                                'hyperlinks': {'checkListLinks': None,
                                          'documentRequisites': None,
                                          'guidelineLinks': None,
                                          'issuingOiv': [],
                                          'reportSuccessLinks': None},
                                'isBasedOnAnother': False,
                                'isPenaltyBasedOnAnother': False,
                                'oivId': 'OIV_00064',
                                'penaltyData': [{'penaltyAdministrativeResponsibilitySubject': [
                                {'code': 'SubjectAdministrationResponsibility_00004',
                                'sanctions': [{'code': 'PenaltyType_001',
                                               'comment': None,
                                               'id': None,
                                               'penaltyId': None},
                                              {'code': 'PenaltyType_002',
                                               'comment': None,
                                               'id': None,
                                               'measure': {'accurate': None,
                                                           'from': 500,
                                                           'measureType': 'range',
                                                           'other': None,
                                                           'to': 1000,
                                                           'valueType': 'rub'},
                                               'penaltyId': None}]},
                                {'code': 'SubjectAdministrationResponsibility_00003',
                                'sanctions': [{'code': 'PenaltyType_001',
                                               'comment': None,
                                               'id': None,
                                               'penaltyId': None},
                                              {'code': 'PenaltyType_002',
                                               'comment': None,
                                               'id': None,
                                               'measure': {'accurate': None,
                                                           'from': 500,
                                                           'measureType': 'range',
                                                           'other': None,
                                                           'to': 1000,
                                                           'valueType': 'rub'},
                                               'penaltyId': None},
                                              {'code': 'PenaltyType_008',
                                               'comment': None,
                                               'id': None,
                                               'measure': {'accurate': None,
                                                           'from': 1,
                                                           'measureType': 'range',
                                                           'other': None,
                                                           'to': 90,
                                                           'valueType': 'day'},
                                               'penaltyId': None}]},
                                               {'code': 'SubjectAdministrationResponsibility_00002',
                                                'sanctions': [{'code': 'PenaltyType_001',
                                                               'comment': None,
                                                               'id': None,
                                                               'penaltyId': None},
                                                              {'code': 'PenaltyType_002',
                                                               'comment': None,
                                                               'id': None,
                                                               'measure': {'accurate': None,
                                                                           'from': 10000,
                                                                           'measureType': 'range',
                                                                           'other': None,
                                                                           'to': 20000,
                                                                           'valueType': 'rub'},
                                                               'penaltyId': None},
                                                              {'code': 'PenaltyType_008',
                                                               'comment': None,
                                                               'id': None,
                                                               'measure': {'accurate': None,
                                                                           'from': 1,
                                                                           'measureType': 'range',
                                                                           'other': None,
                                                                           'to': 90,
                                                                           'valueType': 'day'},
                                                               'penaltyId': None}]}],
                                                        'penaltyAuthority': ['OIV_00064', 'OIV_00032'],
                                                        'penaltyNpaArticle': '6.3',
                                                        'penaltyNpaArticleChapter': '1',
                                                        'penaltyNpaSETitle': None,
                                                        'penaltyNpaTitle': 'PenaltyAct_001',
                                                        'penaltyTitle': 'Ответственность'}]}],
                'mrInstance': {'infiniteValidity': False,
                            'mrEstablishmentObject': ['MREstablishmentObject_00003'],   # refKey
                            'validityEndDate': 1819746000000},
                'suId': seId,
                'titlesAndCheckQuestions': [*ots]}
        request = self.session.post(
            url='https://rg.gov.ru/api/mandatoryRequirements/create',
            json=body,
            headers={
                **self.headers,
                # "referrer":
                #     "https://rg.gov.ru/npa-knd/" + npaId +
                #     "/create-mandatory-requirements/control-types/0/OIV_00064/additional?suId=" + seId +
                #     "&backPath=NpaSuList"
            })
        return request.content

    def sendToSignSE(self, seId, npaId):

        body = {
          "contentType": "SendForSigning",
          "isReady": True,
          "item": {
            "itemClassCode": "MRRecommendation",
            "itemId": seId,
            "agencyId": "OIV_00064"
          }
        }
        self.session.post(
            url="https://rg.gov.ru/api/signature/readyForSigning",
            json=body,
            headers={
                **self.headers,
                "Referer": f"https://rg.gov.ru/npa-knd/{npaId}/structural-unit"
            }
        )





def main(seId, ots: list):
    # ots = [
    #     # {
    #     #     'title': '',
    #     #     'checkQuestion': ''
    #     # },
    #     {
    #         'title': "",
    #         'checkQuestion': "",
    #     },
    #     # {
    #     #     'title': 'Документы, подтверждающие безопасность непереработанного продовольственного (пищевого) сырья животного происхождения, подлежат хранению в течение трех лет со дня их выдачи.',
    #     #     'checkQuestion': 'Документы, подтверждающие безопасность непереработанного продовольственного (пищевого) сырья животного происхождения, хранятся в течение трех лет со дня их выдачи?'
    #     # },
    #
    # ]

    e = Erot()
    result = e.add_ot(
        seId=seId,
        ots=ots,
    )
    pprint(result.content)


def formatQuestion(checkQuestion: str):
    return checkQuestion if checkQuestion.endswith('?') else f'{checkQuestion}?'


def formatTextOT(textOT):
    return textOT if textOT.endswith('.') else f'{textOT}.'

def collect_data_for_adding_ot(seId=None):
    _dict = {
        # 'npaId': input('Введите идентификатор НПА'),
        'seId': input('Введите идентификатор структурной единицы') if not seId else seId,
    }
    ots = []


    print("теперь само введение обязательных требований (текст-проверочный вопрос). для завершения введите stop ")
    stop_words = ['stop', 's', "ыещз", "ы"]
    while True:
        text = input('Введите текст обязательного требования')
        if text in stop_words:
            break
        text = text.strip()
        text = formatTextOT(text)

        checkQuestion = input('введите проверочный вопрос обязательного требования').strip()
        checkQuestion = formatQuestion(checkQuestion)
        print('')
        ots.append(
            {
                'title': text,
                'checkQuestion': checkQuestion,
            }
        )

    _dict['ots'] = ots
    return _dict


def getDataForm():

    translater = {
        "часть": "part",
        "раздел": "section",
        "подраздел": "subsection",
        "глава": "chapter",
        "параграф": "paragraph",
        "статья": "article",
        "пункт": "item",
        "подпункт": "subitem",
        "абзац": "indent",
        "другое": "other",
    },
    formDataRU = {
        "часть": "None",
        "раздел": "None",
        "подраздел": "None",
        "глава": "None",
        "параграф": "None",
        "статья": "None",
        "пункт": "None",
        "подпункт": "None",
        "абзац": "None",
        "другое": "None",
    },
    return dict((translater[0][k], v) for k, v in json.loads(input(f'{formDataRU[0]}\n').replace("'", '"')).items())


def getExelFilePath():
    print(
        'Абсолютный путь до файла - путь начиная с расположения на диске/папке/и тд. Его можно получить через буфер обмена методом "Скопировать путь"')
    print("ВАЖНО!!!")
    print()
    print(
        'Обработка файла будет со второй строки. \nстолбец В - id структурной единицы, \nстолбец С - текст обязательного требования, \nстолбец D - контрольный вопрос.\nУбедитесь, что файл не открыт и сохранен в корректном формате(".xlsx")')
    print()
    print("ВАЖНО!!!")
    paths = input('ВВЕДИТЕ АБСОЛЮТНЫЙ ПУТЬ ДО ОБРАБАТЫВАЕМОГО ФАЙЛА\n')
    path = paths.replace(paths[:1], '').replace(paths[:-1], '')
    return path


def form_ot_from_file():
    filePath = getExelFilePath()
    wb = openpyxl.load_workbook(filePath)
    sh = wb.worksheets[0]
    SEs = []
    currentSE = None
    currentOTs = []
    for row in sh.iter_rows(min_col=2, max_col=4, min_row=2, values_only=True):
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

    e = Erot()

    for se in SEs:
        result = e.add_ot(
            seId=se['seId'],
            ots=se['ots'],
        )
        print(result)
        # print(se['seId'], se['ots'])




def menu():
    print('hot - внести обязательные требования вручную\n'
          'jot - внести обязательные требования из json файла\n'
          'exel - внести обязательные требования из exel файла\n'
          'hse - внести структурную единицу вручную\n'
          'change_se - сменить структурную единицу\n'
          'change_npa - сменить НПА\n'
          )
    stopWord = ['q', 'stop', 's', 'exit', 'break']
    npaId = None
    seId = None

    e = Erot()
    while True:
        command = input('>>>')
        if command in stopWord:
            break
        match command:
            case 'hot':
                if not seId:
                    seId = input('Введите идентификатор структурной единицы')
                _dict = collect_data_for_adding_ot(seId)
                print(_dict)
                result = e.add_ot(
                    seId=_dict['seId'],
                    ots=_dict['ots']
                )
                pprint(result)
            case 'jot':
                _dict = json.loads(input('Введите JSON как строку...').replace("'", '"'))
                result = e.add_ot(
                    seId=_dict['seId'],
                    ots=_dict['ots']
                )
                pprint(result)
            case 'hse':
                if not npaId:
                    npaId = input('Введите идентификатор НПА')
                seId = e.add_se(
                    npaId=npaId,
                    text=input('введите текст структурной единицы'),
                    formData=getDataForm()
                )

            case 'exel':
                form_ot_from_file()

            case 'change_se':
                seId = input('Введите идентификатор структурной единицы')

            case 'change_npa':
                npaId = input('Введите идентификатор НПА')










if __name__ == '__main__':

    menu()
    # print(form_ot_from_file("S:\Зайцев_АД\ерот 3686.xlsx"))
    # print(getDataForm())
    # print(collect_data_for_adding_ot())
    # ots = [
    #     # {
    #     #     'title': '',
    #     #     'checkQuestion': ''
    #     # },
    #     {
    #         'title': "Сведения о регистрации пищевой продукции нового вида вносятся в единый реестр пищевой продукции нового вида.",
    #         'checkQuestion': "Сведения о регистрации пищевой продукции нового вида вносятся в единый реестр пищевой продукции нового вида?",
    #     },
    #     # {
    #     #     'title': 'Документы, подтверждающие безопасность непереработанного продовольственного (пищевого) сырья животного происхождения, подлежат хранению в течение трех лет со дня их выдачи.',
    #     #     'checkQuestion': 'Документы, подтверждающие безопасность непереработанного продовольственного (пищевого) сырья животного происхождения, хранятся в течение трех лет со дня их выдачи?'
    #     # },
    #
    # ]
    # ots = [{'title': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должен разрабатываться, внедряться и поддерживаться выбор необходимых для обеспечения безопасности пищевой продукции технологических процессов производства (изготовления) пищевой продукции.', 'checkQuestion': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) разрабатывается, внедряется и поддерживается выбор необходимых для обеспечения безопасности пищевой продукции технологических процессов производства (изготовления) пищевой продукции?'}, {'title': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должен разрабатываться, внедряться и поддерживаться выбор последовательности и поточности технологических операций производства (изготовления) пищевой продукции с целью исключения загрязнения продовольственного (пищевого) сырья и пищевой продукции.', 'checkQuestion': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должен разрабатывается, внедряется и поддерживается выбор последовательности и поточности технологических операций производства (изготовления) пищевой продукции с целью исключения загрязнения продовольственного (пищевого) сырья и пищевой продукции?'}, {'title': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должно разрабатываться, внедряться и поддерживаться определение контролируемых этапов технологических операций и пищевой продукции на этапах ее производства (изготовления) в программах производственного контроля.', 'checkQuestion': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) разрабатывается, внедряется и поддерживается определение контролируемых этапов технологических операций и пищевой продукции на этапах ее производства (изготовления) в программах производственного контроля?'}, {'title': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должно разрабатываться, внедряться и поддерживаться проведение контроля за продовольственным (пищевым) сырьем, технологическими средствами, упаковочными материалами, изделиями, используемыми при производстве (изготовлении) пищевой продукции, а также за пищевой продукцией средствами, обеспечивающими необходимые достоверность и полноту контроля.', 'checkQuestion': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) разрабатывается, внедряется и поддерживается проведение контроля за продовольственным (пищевым) сырьем, технологическими средствами, упаковочными материалами, изделиями, используемыми при производстве (изготовлении) пищевой продукции, а также за пищевой продукцией средствами, обеспечивающими необходимые достоверность и полноту контроля?'}, {'title': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должно разрабатываться, внедряться и поддерживаться проведение контроля за функционированием технологического оборудования в порядке, обеспечивающем производство (изготовление) пищевой продукции, соответствующей требованиям настоящего технического регламента и (или) технических регламентов Таможенного союза на отдельные виды пищевой продукции.', 'checkQuestion': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) разрабатывается, внедряется и поддерживается проведение контроля за функционированием технологического оборудования в порядке, обеспечивающем производство (изготовление) пищевой продукции, соответствующей требованиям настоящего технического регламента и (или) технических регламентов Таможенного союза на отдельные виды пищевой продукции?'}, {'title': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должно разрабатываться, внедряться и поддерживаться обеспечение документирования информации о контролируемых этапах технологических операций и результатов контроля пищевой продукции.', 'checkQuestion': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) разрабатывается, внедряется и поддерживается обеспечение документирования информации о контролируемых этапах технологических операций и результатов контроля пищевой продукции?'}, {'title': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должно разрабатываться, внедряться и поддерживаться соблюдение условий хранения и перевозки (транспортирования) пищевой продукции.', 'checkQuestion': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) разрабатывается, внедряется и поддерживается соблюдение условий хранения и перевозки (транспортирования) пищевой продукции?'}, {'title': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должно разрабатываться, внедряться и поддерживаться содержание производственных помещений, технологического оборудования и инвентаря, используемых в процессе производства (изготовления) пищевой продукции, в состоянии, исключающем загрязнение пищевой продукции.', 'checkQuestion': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) разрабатывается, внедряется и поддерживается содержание производственных помещений, технологического оборудования и инвентаря, используемых в процессе производства (изготовления) пищевой продукции, в состоянии, исключающем загрязнение пищевой продукции?'}, {'title': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должен разрабатываться, внедряться и поддерживаться выбор способов и обеспечение соблюдения работниками правил личной гигиены в целях обеспечения безопасности пищевой продукции.', 'checkQuestion': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) разрабатывается, внедряется и поддерживается выбор способов и обеспечение соблюдения работниками правил личной гигиены в целях обеспечения безопасности пищевой продукции?'}, {'title': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должен разрабатываться, внедряться и поддерживаться выбор обеспечивающих безопасность пищевой продукции способов, установление периодичности и проведение уборки, мойки, дезинфекции, дезинсекции и дератизации производственных помещений, технологического оборудования и инвентаря, используемых в процессе производства (изготовления) пищевой продукции.', 'checkQuestion': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) разрабатывается, внедряется и поддерживается выбор обеспечивающих безопасность пищевой продукции способов, установление периодичности и проведение уборки, мойки, дезинфекции, дезинсекции и дератизации производственных помещений, технологического оборудования и инвентаря, используемых в процессе производства (изготовления) пищевой продукции?'}, {'title': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должно разрабатываться, внедряться и поддерживаться ведение и хранение документации на бумажных и (или) электронных носителях, подтверждающей соответствие произведенной пищевой продукции требованиям, установленным настоящим техническим регламентом и (или) техническими регламентами Таможенного союза на отдельные виды пищевой продукции.', 'checkQuestion': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) разрабатывается, внедряется и поддерживается ведение и хранение документации на бумажных и (или) электронных носителях, подтверждающей соответствие произведенной пищевой продукции требованиям, установленным настоящим техническим регламентом и (или) техническими регламентами Таможенного союза на отдельные виды пищевой продукции?'}, {'title': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) должна разрабатываться, внедряться и поддерживаться прослеживаемость пищевой продукции.', 'checkQuestion': 'Для обеспечения безопасности пищевой продукции в процессе ее производства (изготовления) разрабатывается, внедряется и поддерживается прослеживаемость пищевой продукции?'}]
    # main(
    #     npaId="af953092-fd67-4b8e-bff1-b3510170e180",
    #     seId="6530e0ab-9139-488d-a7c6-1766542600f3",
    #     ots=ots
    # )

