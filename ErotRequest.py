import requests
from config import Zaitsev_knd
from crypto import Crypto


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
        self.session.post(url="https://rg.gov.ru/mzi/auth/signIn", json=body, headers=self.headers)

    def add_ot(self, npaId, seId, ots):
        # ots its a list ot like {'checkQuestion': checkQuestion, 'title': title}
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
                            'mrEstablishmentObject': ['MREstablishmentObject_00003'],
                            'validityEndDate': 1819746000000},
                'suId': seId,
                'titlesAndCheckQuestions': [*ots]}
        request = self.session.post(
            url='https://rg.gov.ru/api/mandatoryRequirements/create',
            json=body,
            headers={
                **self.headers,
                "referrer":
                    "https://rg.gov.ru/npa-knd/" + npaId +
                    "/create-mandatory-requirements/control-types/0/OIV_00064/additional?suId=" + seId +
                    "&backPath=NpaSuList"
            })
        return request


def main():
    ots = [
        # {
        #     'title': '',
        #     'checkQuestion': ''
        # },
        {
            'title': "Больные инфекционными заболеваниями, лица с подозрением на такие заболевания, лица, контактировавшие с больными инфекционными заболеваниями, лица, являющиеся носителями возбудителей инфекционных заболеваний, не допускаются к работам, связанным с производством (изготовлением) пищевой продукции",
            'checkQuestion': "Допускаются ли к работам, связанным с производством (изготовлением) пищевой продукции, больные инфекционными заболеваниями, лица с подозрением на такие заболевания, лица, контактировавшие с больными инфекционными заболеваниями, лица, являющиеся носителями возбудителей инфекционных заболеваний?",
        },
        # {
        #     'title': 'Документы, подтверждающие безопасность непереработанного продовольственного (пищевого) сырья животного происхождения, подлежат хранению в течение трех лет со дня их выдачи.',
        #     'checkQuestion': 'Документы, подтверждающие безопасность непереработанного продовольственного (пищевого) сырья животного происхождения, хранятся в течение трех лет со дня их выдачи?'
        # },

    ]

    e = Erot()
    result = e.add_ot(
        npaId="af953092-fd67-4b8e-bff1-b3510170e180",
        seId="ba0731c3-36a4-4581-ad3e-d43c29d0bea0",
        ots=ots,
    )
    print(result.content)


if __name__ == '__main__':
    main()

