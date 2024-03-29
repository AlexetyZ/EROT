import re

exceptions = {
    'нефть': {
        'gent': 'нефти',
        'datv': 'нефть',
        'accs': 'нефть',
        'ablt': 'нефтью',
        'loct': 'нефти',
    },
    'эфир': {
        'gent': 'эфира',
        'datv': 'эфиру',
        'accs': 'эфир',
        'ablt': 'эфиром',
        'loct': 'эфире',
    },
    'эфиры': {
        'gent': 'эфиров',
        'datv': 'эфирам',
        'accs': 'эфиры',
        'ablt': 'эфирами',
        'loct': 'эфирах',
    },
    'олово': {
        'gent': 'олова',
        'datv': 'олову',
        'accs': 'олово',
        'ablt': 'оловом',
        'loct': 'олове',
    },
    'яйца': {
        'gent': 'яиц',
        'datv': 'яйцам',
        'accs': 'яйца',
        'ablt': 'яйцами',
        'loct': 'яйцах',
    },
    'яйцо': {
        'gent': 'яйца',
        'datv': 'яйцу',
        'accs': 'яйцо',
        'ablt': 'яйцом',
        'loct': 'яйце',
    },
    'цисты': {
        'gent': 'цист',
        'datv': 'цистам',
        'accs': 'цисты',
        'ablt': 'цистами',
        'loct': 'цистах',
    },
    'ооцисты': {
        'gent': 'ооцист',
        'datv': 'ооцистам',
        'accs': 'ооцисты',
        'ablt': 'ооцистами',
        'loct': 'ооцистах',
    },
    'овоцисты': {
        'gent': 'овоцист',
        'datv': 'овоцистам',
        'accs': 'овоцисты',
        'ablt': 'овоцистами',
        'loct': 'овоцистах',
    },
    'ооциста': {
        'gent': 'ооцисты',
        'datv': 'ооцисте',
        'accs': 'ооцисту',
        'ablt': 'ооцистой',
        'loct': 'ооцисте',
    },
    'овоциста': {
        'gent': 'овоцисты',
        'datv': 'овоцисте',
        'accs': 'овоцисту',
        'ablt': 'овоцистой',
        'loct': 'овоцисте',
    },
    r'\D+итол': {
        'gent': r'\D+итола',
        'datv': r'\D+итолу',
        'accs': r'\D+итол',
        'ablt': r'\D+итолом',
        'loct': r'\D+итоле',
    },
    'этилкарбитолы': {
        'gent': 'этилкарбитолов',
        'datv': 'этилкарбитолам',
        'accs': 'этилкарбитолы',
        'ablt': 'этилкарбитолами',
        'loct': 'этилкарбитолах',
    },
    'этилкарбитол': {
        'gent': 'этилкарбитола',
        'datv': 'этилкарбитолу',
        'accs': 'этилкарбитол',
        'ablt': 'этилкарбитолом',
        'loct': 'этилкарбитоле',
    },
    'карбонат': {
        'gent': 'карбоната',
        'datv': 'карбонату',
        'accs': 'карбонат',
        'ablt': 'карбонатом',
        'loct': 'карбонате',
    },
    'спирт': {
        'gent': 'спирта',
        'datv': 'спирту',
        'accs': 'спирт',
        'ablt': 'спиртом',
        'loct': 'спирте',
    },
    'бутоксиэтилен': {
        'gent': 'бутоксиэтилена',
        'datv': 'бутоксиэтилену',
        'accs': 'бутоксиэтилен',
        'ablt': 'бутоксиэтиленом',
        'loct': 'бутоксиэтилене',
    },
    'соль': {
        'gent': 'соли',
        'datv': 'соли',
        'accs': 'соль',
        'ablt': 'солью',
        'loct': 'соли',
    },
    'боксит': {
        'gent': 'боксита',
        'datv': 'бокситу',
        'accs': 'боксит',
        'ablt': 'бокситом',
        'loct': 'боксите',
    },
    'нефелин': {
        'gent': 'нефелина',
        'datv': 'нефелину',
        'accs': 'нефелин',
        'ablt': 'нефелином',
        'loct': 'нефелине',
    },
    'спек': {
        'gent': 'спека',
        'datv': 'спеку',
        'accs': 'спек',
        'ablt': 'спеком',
        'loct': 'спеке',
    },
    'молибден': {
        'gent': 'молибдена',
        'datv': 'молибдену',
        'accs': 'молибден',
        'ablt': 'молибденом',
        'loct': 'молибдене',
    },
    'мышьяк': {
        'gent': 'мышьяка',
        'datv': 'мышьяку',
        'accs': 'мышьяк',
        'ablt': 'мышьяком',
        'loct': 'мышьяке',
    },
    'эприн': {
        'gent': 'эприна',
        'datv': 'эприну',
        'accs': 'эприн',
        'ablt': 'эприном',
        'loct': 'эприне',
    },
    'ен': {
        'gent': 'ена',
        'datv': 'ену',
        'accs': 'ен',
        'ablt': 'еном',
        'loct': 'ене',
    },
    'продукты': {
        'gent': 'продуктов',
        'datv': 'продуктам',
        'accs': 'продукты',
        'ablt': 'продуктами',
        'loct': 'продуктах',
    },
    'шлак': {
        'gent': 'шлака',
        'datv': 'шлаку',
        'accs': 'шлак',
        'ablt': 'шлаком',
        'loct': 'шлаке',
    },
    'молотый': {
        'gent': 'молотого',
        'datv': 'молотому',
        'accs': 'молотый',
        'ablt': 'молотым',
        'loct': 'молотом',
    },
    'цинк': {
        'gent': 'цинка',
        'datv': 'цинку',
        'accs': 'цинк',
        'ablt': 'цинком',
        'loct': 'цинке',
    },
    'эрбумин': {
        'gent': 'эрбумина',
        'datv': 'эрбумину',
        'accs': 'эрбумин',
        'ablt': 'эрбумином',
        'loct': 'эрбумине',
    },
    'кораксан': {
        'gent': 'кораксана',
        'datv': 'кораксану',
        'accs': 'кораксан',
        'ablt': 'кораксаном',
        'loct': 'кораксане',
    },
    'кетопрофен': {
        'gent': 'кетопрофена',
        'datv': 'кетопрофену',
        'accs': 'кетопрофен',
        'ablt': 'кетопрофеном',
        'loct': 'кетопрофене',
    },
    'флокумафен': {
        'gent': 'флокумафена',
        'datv': 'флокумафену',
        'accs': 'флокумафен',
        'ablt': 'флокумафеном',
        'loct': 'флокумафене',
    },
    'сухой': {
        'gent': 'сухого',
        'datv': 'сухому',
        'accs': 'сухой',
        'ablt': 'сухим',
        'loct': 'сухом',
    },
    'тилаксин': {
        'gent': 'тилаксина',
        'datv': 'тилаксину',
        'accs': 'тилаксин',
        'ablt': 'тилаксином',
        'loct': 'тилаксине',
    },
    'гамма': {
        'gent': 'гамма',
        'datv': 'гамма',
        'accs': 'гамма',
        'ablt': 'гамма',
        'loct': 'гамма',
    },
    'альфа': {
        'gent': 'альфа',
        'datv': 'альфа',
        'accs': 'альфа',
        'ablt': 'альфа',
        'loct': 'альфа',
    },
    'бета': {
        'gent': 'бета',
        'datv': 'бета',
        'accs': 'бета',
        'ablt': 'бета',
        'loct': 'бета',
    },
    'зарин': {
        'gent': 'зарина',
        'datv': 'зарину',
        'accs': 'зарин',
        'ablt': 'зарином',
        'loct': 'зарине',
    },
    'кабинет': {
        'gent': 'кабинета',
        'datv': 'кабинету',
        'accs': 'кабинет',
        'ablt': 'кабинетом',
        'loct': 'кабинете',
    },
    'помещение': {
        'gent': 'помещения',
        'datv': 'помещению',
        'accs': 'помещение',
        'ablt': 'помещением',
        'loct': 'помещении',
    },
    'зал': {
        'gent': 'зала',
        'datv': 'залу',
        'accs': 'зал',
        'ablt': 'залом',
        'loct': 'зале',
    },
    'кабинеты': {
        'gent': 'кабинетов',
        'datv': 'кабинетам',
        'accs': 'кабинеты',
        'ablt': 'кабинетами',
        'loct': 'кабинетах',
    },
    'аудитория': {
        'gent': 'аудитории',
        'datv': 'аудитории',
        'accs': 'аудиторию',
        'ablt': 'аудиторией',
        'loct': 'аудитории',
    },
    'аудитории': {
        'gent': 'аудиторий',
        'datv': 'аудиториям',
        'accs': 'аудитории',
        'ablt': 'аудиториями',
        'loct': 'аудиториях',
    },
    'планшет': {
        'gent': 'планшета',
        'datv': 'планшету',
        'accs': 'планшет',
        'ablt': 'планшетом',
        'loct': 'планшете',
    },
    'планшеты': {
        'gent': 'планшетов',
        'datv': 'планшетам',
        'accs': 'планшеты',
        'ablt': 'планшетами',
        'loct': 'планшетах',
    },
    'раковины': {
        'gent': 'раковин',
        'datv': 'раковинам',
        'accs': 'раковины',
        'ablt': 'раковинами',
        'loct': 'раковинах',
    },
    'раковина': {
        'gent': 'раковины',
        'datv': 'раковине',
        'accs': 'раковину',
        'ablt': 'раковиной',
        'loct': 'раковине',
    },
    'ванна': {
        'gent': 'ванны',
        'datv': 'ванне',
        'accs': 'ванну',
        'ablt': 'ванной',
        'loct': 'ванне',
    },
    'ванны': {
        'gent': 'ванн',
        'datv': 'ваннам',
        'accs': 'ванны',
        'ablt': 'ваннами',
        'loct': 'ваннах',
    },
    'машина': {
        'gent': 'машины',
        'datv': 'машине',
        'accs': 'машину',
        'ablt': 'машиной',
        'loct': 'машине',
    },
    'машины': {
        'gent': 'машин',
        'datv': 'машинам',
        'accs': 'машины',
        'ablt': 'машинами',
        'loct': 'машинах',
    },
    'залы': {
        'gent': 'залы',
        'datv': 'залам',
        'accs': 'залы',
        'ablt': 'залами',
        'loct': 'залах',
    },
    'гардероб': {
        'gent': 'гардероба',
        'datv': 'гардеробу',
        'accs': 'гардероб',
        'ablt': 'гардеробом',
        'loct': 'гардеробе',
    },
    'гардеробы': {
        'gent': 'гардеробов',
        'datv': 'гардеробам',
        'accs': 'гардеробы',
        'ablt': 'гардеробами',
        'loct': 'гардеробах',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
}

reg_ex_dict = {
    r'ция$': {
        'gent': 'ции',
        'datv': 'ции',
        'accs': 'цию',
        'ablt': 'цией',
        'loct': 'ции',
    },
    r'вные$': {
        'gent': 'вных',
        'datv': 'вным',
        'accs': 'вные',
        'ablt': 'вными',
        'loct': 'вных',
    },
    r'вный$': {
        'gent': 'вного',
        'datv': 'вному',
        'accs': 'вный',
        'ablt': 'вным',
        'loct': 'вном',
    },
    r'вная$': {
        'gent': 'вной',
        'datv': 'вной',
        'accs': 'вную',
        'ablt': 'вной',
        'loct': 'вной',
    },
    r'ание$': {
        'gent': 'ания',
        'datv': 'анию',
        'accs': 'ание',
        'ablt': 'анием',
        'loct': 'ании',
    },
    r'дания$': {
        'gent': 'даний',
        'datv': 'даниям',
        'accs': 'дания',
        'ablt': 'даниями',
        'loct': 'даниях',
    },
    r'ность$': {
        'gent': 'ности',
        'datv': 'ности',
        'accs': 'ность',
        'ablt': 'ностью',
        'loct': 'ности',
    },
    r'щение$': {
        'gent': 'щения',
        'datv': 'щению',
        'accs': 'щение',
        'ablt': 'щением',
        'loct': 'щении',
    },
    r'щения$': {
        'gent': 'щений',
        'datv': 'щениям',
        'accs': 'щения',
        'ablt': 'щениями',
        'loct': 'щениях',
    },
    r'ельная$': {
        'gent': 'ельной',
        'datv': 'ельной',
        'accs': 'ельную',
        'ablt': 'ельной',
        'loct': 'ельной',
    },
    r'ельные$': {
        'gent': 'ельных',
        'datv': 'ельным',
        'accs': 'ельные',
        'ablt': 'ельными',
        'loct': 'ельных',
    },
    r'ебные$': {
        'gent': 'ебных',
        'datv': 'ебным',
        'accs': 'ебные',
        'ablt': 'ебными',
        'loct': 'ебных',
    },
    r'ната$': {
        'gent': 'наты',
        'datv': 'нате',
        'accs': 'нату',
        'ablt': 'натой',
        'loct': 'нате',
    },

    r'льский$': {
        'gent': 'льского',
        'datv': 'льскому',
        'accs': 'льский',
        'ablt': 'льским',
        'loct': 'льском',
    },
    r'льские$': {
        'gent': 'льских',
        'datv': 'льским',
        'accs': 'льские',
        'ablt': 'льскими',
        'loct': 'льских',
    },
    r'товые$': {
        'gent': 'товых',
        'datv': 'товым',
        'accs': 'товые',
        'ablt': 'товыми',
        'loct': 'товых',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },
    'пусто': {
        'gent': '',
        'datv': '',
        'accs': '',
        'ablt': '',
        'loct': '',
    },

}


def reg_dict_assistent(w, case=None) -> str or bool:
    """
    :param w: опытное слово - слово, испытывается на наличие его окончания (регулярным выражением) в словаре регулярных
    выражений. С целью найти подходящее окончание. ТОЛЬКО ОКОНЧАНИЕ, БЛЯДЬ, А НЕ ЧАСТИ СЛОВА В СЕРЕДИНЕ!!! НЕ ЗАБУДЬ ОПЯТЬ!!!
    :param case: Падеж, на который следует изменить опытное слово, от него зависит подбираемое окончание.
    :return: Опытное слово в установленном падеже, при отсутстии параметра case вернутся буловое значение в зависимости от наличия окончания в словаре
    """
    for key, value in reg_ex_dict.items():
        searching = re.search(key, w)
        if searching:
            if case is None:
                return True
            return searching.string[:searching.start()] + value[
                case]  # соединяет первые символы опытного слова за исключением искомого выражения и соединяет с соответствующим выражением в зависимости от падежа
    return False