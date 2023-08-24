users = {
    "Богдан" : -1001878784957,
    "Павло"  : -1001951660203,
    "Антон"  : -1001872611994,
    "Оксана" : -995036647,
}

users_revers = {value: key for key, value in users.items()}

data = {
    # Я
    users['Богдан']: {
        'Ноутбук дешевий':{
            'filterDelete':
            [
                'Windows xp', 'Windows 7', 'Windows 8',

                'celeron', 'pentium', 'amd', 'Athlon',
                'apple', 'mac',
                'i3 M',
                'i3-1', 'i3-2', 'i3-3', 'i3-4', 'i3-5', 'i3-6','i3-7',
                'i5-1', 'i5-2', 'i5-3', 'i5-4',
                'i7-1', 'i7-2', 'i7-3',
                'i3 1', 'i3 2', 'i3 3', 'i3 4', 'i3 5', 'i3 6', 'i3 7',
                'i5 1', 'i5 2', 'i5 3', 'i5 4',
                'i7 1', 'i7 2', 'i7 3',

                '2gb ram','3gb ram','4gb ram','6gb ram',
                'RAM 2 Gb','RAM 4 Gb','RAM 6 Gb',
                '4/32 GB',
                'DDR2',

                '11.6\"', '12.5\"', '13.3', '14\"',
                '1600x900', '1366x768',
                '1600*900', '1366*768',

                "1660, мощнее 3050 ti",
                
            ],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/elektronika/noutbuki-i-aksesuary/noutbuki/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=3000&search%5Bfilter_float_price:to%5D=8000&search%5Bfilter_enum_state%5D%5B0%5D=used'
        },
        'Ноутбук дорогий':{
            'filterDelete':[
                'apple','mac','MacBook',
                'celeron', 'pentium', 'Pentium', 'amd', 'Athlon', 'Core 2 Duo',
                'i3',

                'RAM 4 Gb','RAM 6 Gb',
                '4gb ram','6gb ram',
                'DDR2','DDR3',

                '11.6\"','12.5\"','13.3','14\"',
                '1600x900', '1366x768',
                '1600*900', '1366*768',

                "MX 2gb",

                "1660, мощнее 3050 ti",
                
            ],
            'filterFind':[
                '1660', 
                'rtx3', 'rtx4', 
                'rtx 3', 'rtx 4', 
                'gtx 10', 'gtx10', 'gtx-10', 
                'i5 8','i5 9','i5 10',
                'i5-8','i5-9','i5-10',
                'i7 8','i7 9','i7 10',
                'i7-8','i7-9','i7-10',
                'i9',
                '4800h',
                '16', '32',
                'ti',
                ],
            'link':'https://www.olx.ua/uk/elektronika/noutbuki-i-aksesuary/noutbuki/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:to%5D=13000'
        },
        'Батарея':{
            'filterDelete':
            [],
            'filterFind':
            [
                'електросамокат',
                'електричний самокат',
                'самокат на електроприводі',
                'е-самокат',
                'электросамокат',
                'электрический самокат',
                'самокат с электроприводом',
                'э-самокат',
                'самокат',
                'куго',
                'кугго',
                'Занимаюсь ремонтом',
            ],
            'link':'https://www.olx.ua/uk/list/q-%D0%B1%D0%B0%D1%82%D0%B0%D1%80%D0%B5%D1%8F/?search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=100&search%5Bfilter_float_price:to%5D=1000'
        },
        'Електросамокат':{
            'filterDelete':[],
            'filterFind':[
                'kugoo', 
                'kugo', 
                's3',
                'куго',
                'кугоо',
                'кугго',
            ],
            'link':'https://www.olx.ua/uk/transport/moto/elektrosamokaty-hiroskutery/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=100&search%5Bfilter_float_price:to%5D=4500'
        },
        'Лот':{
            'filterDelete':[
                'Лист марок',

                'dendy', 'денді',
                'диски с играми',
                'гарантія',
                'навушники',
                'Навушники наушники',


                'Видеокамера','Відеокамера',
                'видеомагнитофон','відеомагнітофон',
                'Картридж HP',
                'фотопринадлежности',            
                'Батерейки літієві CR1225',            

                'Спутниковый тюнер','Супутниковий тюнер',

                'iPhone',
                'Лот телефонів',
                'Лот сенсорних телефонів',

                'Процесор',
                'Ноутбуки оптом',
                'Радиаторы процессоров',            
                'шлейф для видеокарты',            
                'удлинитель АТХ',            

                'ВСЕ НОВЕ',            
                'поплавок',            
                'Часы цифровые',            
                'Советским',            
                'вещи новые',            

            ],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/elektronika/q-%D0%BB%D0%BE%D1%82/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=100&search%5Bfilter_float_price:to%5D=1000'
        },
        'xiaomi mi 9t':{
            'filterDelete':[
                'Гидрогелевая пленка',
                'Гидрогелевая плёнка',
                'Поліуретанова плівка',
                'Дисплей для Samsung',
                'протиударні  чохли',
                'Патріотичні Чохли',
                'Чохол протиударний для Xiaomi',
            ],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/elektronika/telefony-i-aksesuary/q-xiaomi-mi-9t/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=100&search%5Bfilter_float_price:to%5D=1000'
        },
        'xiaomi redmi note 7':{
            'filterDelete':[
                '32',
            ],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/elektronika/telefony-i-aksesuary/q-xiaomi-redmi-note-7/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=500&search%5Bfilter_float_price:to%5D=2000'
        },
        'кімната':{
            'filterDelete':['дівч'],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/nedvizhimost/komnaty/dolgosrochnaya-arenda-komnat/lutsk/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:to%5D=2500'
        },
        'блендер єбош':{
            'filterDelete':['boch'],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/dom-i-sad/posuda-kuhonnaya-utvar/q-bosch/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=100&search%5Bfilter_float_price:to%5D=500&search%5Bfilter_enum_state%5D%5B0%5D=used'
        },
    },
    users['Павло'] : {
        'лот електроніки':{
            'filterDelete':[],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/elektronika/noutbuki-i-aksesuary/noutbuki/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=1&search%5Bfilter_float_price:to%5D=1000&search%5Bfilter_enum_state%5D%5B0%5D=used'
        },
        'кімната':{
            'filterDelete':[],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/nedvizhimost/komnaty/dolgosrochnaya-arenda-komnat/lutsk/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:to%5D=3000'
        },
        'кімната2':{
            'filterDelete':[],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/nedvizhimost/lutsk/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=100&search%5Bfilter_float_price:to%5D=3000'
        },
    },
    users['Антон'] : {
        'лот електроніки':{
            'filterDelete':[],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/elektronika/q-%D0%BB%D0%BE%D1%82-%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D1%96%D0%BA%D0%B8/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:to%5D=1000'
        },
        'все разом':{
            'filterDelete':[
                'локонов', 'Локоны', 'Плойка', 'плойку', 'мясорубки', 'волосся',
                'Можливий опт',
            ],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/elektronika/q-%D0%B2%D1%81%D0%B5-%D1%80%D0%B0%D0%B7%D0%BE%D0%BC/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:to%5D=1000'
        },
        'під ремонт':{
            'filterDelete':[],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/elektronika/q-%D0%BF%D1%96%D0%B4-%D1%80%D0%B5%D0%BC%D0%BE%D0%BD%D1%82/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:to%5D=1000'
        },
        'под ремонт':{
            'filterDelete':[
                'Холодильник',
                'Телевизор',
                'Пральна', 'Стиральная',

                'Домашний телефон',
            ],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/elektronika/q-%D0%BF%D0%BE%D0%B4-%D1%80%D0%B5%D0%BC%D0%BE%D0%BD%D1%82/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:to%5D=1000'
        }
    },
    users['Оксана'] : {
        'книжечки усі':{
            'filterDelete':[
                "російською",
                "клас",
                "зно",
                "Ё", 
                "Э", 
                "дитячі", 
                "казок", 
                "казк", 
                "ссср", 
                "гетьмани", 
                "Майнкрафт", 
                "козацтво", 
                "Народні", 
                "Набор", 
                "підручник", 
            ],
            'filterFind':[],
            'link':'https://www.olx.ua/uk/hobbi-otdyh-i-sport/knigi-zhurnaly/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=0&search%5Bfilter_float_price:to%5D=300'
        },
        'книжечки лише вибрані':{
            'filterDelete':[],
            'filterFind':[
                'англійськ',
                'english',
                'художня',
            ],
            'link':'https://www.olx.ua/uk/hobbi-otdyh-i-sport/knigi-zhurnaly/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=0&search%5Bfilter_float_price:to%5D=400'
        },
    }
}