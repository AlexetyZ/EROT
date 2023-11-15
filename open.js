function enterOT(npaId, seId, title, checkQuestion) {
    (async () => {
        const response = await fetch("https://rg.gov.ru/api/mandatoryRequirements/create", {
          "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "ru,en;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
          },
          "referrer": "https://rg.gov.ru/npa-knd/" + npaId + "/create-mandatory-requirements/control-types/0/OIV_00064/additional?suId=" + seId + "&backPath=NpaSuList",
          "referrerPolicy": "strict-origin-when-cross-origin",
          "body": JSON.stringify({"suId":seId,"titlesAndCheckQuestions":[{"title": title,"checkQuestion": checkQuestion}],"mrInstance":{"validityEndDate":1819746000000,"infiniteValidity":false,"mrEstablishmentObject":["MREstablishmentObject_00003"]},"mrBlocks":[{"controlTypeId":"GovernmentControlKind_00002","isBasedOnAnother":false,"isPenaltyBasedOnAnother":false,"oivId":"OIV_00064","commonInfo":{"categoriesOfPersons":["CategoryOfPersons_04","CategoryOfPersons_01","CategoryOfPersons_02","CategoryOfPersons_03"],"categoriesOfPersonsOtherTitle":null,"assessmentForm":["AssessmentForm_01"],"interestedFOIV":["OIV_00064"],"publicRelationSpheres":["PublicRelationSpheres_00024","PublicRelationSpheres_00023","PublicRelationSpheres_00011","PublicRelationSpheres_00017","PublicRelationSpheres_00013","PublicRelationSpheres_00003","PublicRelationSpheres_00004","PublicRelationSpheres_00001","PublicRelationSpheres_00002","PublicRelationSpheres_00030","PublicRelationSpheres_00027","PublicRelationSpheres_00038","PublicRelationSpheres_00046","PublicRelationSpheres_00025","PublicRelationSpheres_00026","PublicRelationSpheres_00077","PublicRelationSpheres_00053","PublicRelationSpheres_00018","PublicRelationSpheres_00009","PublicRelationSpheres_00008","PublicRelationSpheres_00010"],"activitySubtype":["00","39","86"]},"additionalInfo":{"files":null,"documentReleaseFOIV":[],"documentReleaseFOIVOther":null,"costEstimationFiles":[]},"penaltyData":[{"penaltyNpaTitle":"PenaltyAct_001","penaltyTitle":"Ответственность","penaltyNpaArticle":"6.3","penaltyNpaArticleChapter":"1","penaltyNpaSETitle":null,"penaltyAuthority":["OIV_00064","OIV_00032"],"penaltyAdministrativeResponsibilitySubject":[{"code":"SubjectAdministrationResponsibility_00004","sanctions":[{"penaltyId":null,"id":null,"code":"PenaltyType_001","comment":null},{"penaltyId":null,"id":null,"code":"PenaltyType_002","measure":{"measureType":"range","valueType":"rub","accurate":null,"from":500,"to":1000,"other":null},"comment":null}]},{"code":"SubjectAdministrationResponsibility_00003","sanctions":[{"penaltyId":null,"id":null,"code":"PenaltyType_001","comment":null},{"penaltyId":null,"id":null,"code":"PenaltyType_002","measure":{"measureType":"range","valueType":"rub","accurate":null,"from":500,"to":1000,"other":null},"comment":null},{"penaltyId":null,"id":null,"code":"PenaltyType_008","measure":{"measureType":"range","valueType":"day","accurate":null,"from":1,"to":90,"other":null},"comment":null}]},{"code":"SubjectAdministrationResponsibility_00002","sanctions":[{"penaltyId":null,"id":null,"code":"PenaltyType_001","comment":null},{"penaltyId":null,"id":null,"code":"PenaltyType_002","measure":{"measureType":"range","valueType":"rub","accurate":null,"from":10000,"to":20000,"other":null},"comment":null},{"penaltyId":null,"id":null,"code":"PenaltyType_008","measure":{"measureType":"range","valueType":"day","accurate":null,"from":1,"to":90,"other":null},"comment":null}]}]}],"hyperlinks":{"checkListLinks":null,"guidelineLinks":null,"issuingOiv":[],"documentRequisites":null,"reportSuccessLinks":null}}]}),
          "method": "POST",
          "mode": "cors",
          "credentials": "include"
        });
    })();
}