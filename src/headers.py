# Урлы сервисов с данными + 1hmm
URL = {
    'url_del_time':          'http://185.63.190.188/trade82new/hs/Service/AIExchange/ВремяПоставкиТоваров',
    'url_stat_to_1hmm':      'https://hypermarketmebel.ru/api/product/importDeliveryTimes/?token=aG1tQWNjZXNzVG9rZW4=',
    'url_stat_to_1hmm_test': 'http://ash.dev.1hmm.ru/api/product/importDeliveryTimes/?token=aG1tQWNjZXNzVG9rZW4=',
    'url_for_graphics':      'https://hypermarketmebel.ru/tools/importDeliveryTime.php',
    'url_for_graphics_test': 'http://star.dev.1hmm.ru/tools/importDeliveryTime.php'
}

# Типы поставок товаров
DELIVERY_TYPE = {
    'fabricator':    "От поставщиков",
    'free_balances': "Со свободных остатков"
}

# Логин/пароль базовой авторизации HTTP
HTTP_AUTHORIZATION = {
    'login':    'Web',
    'password': 'WebMarket'
}

# Задержка отправки статистики на 1hmm
SERVICE_DELAY = {
    'one_week': 604800,
    'one_day':  86400,
    'one_hour': 3600
}

# Пути
PATH_DATA = {
    'statistics.json':  '../service_files/statistics.json',
    'stat_graph.json':  '../service_files/stat_graph.json',
    'delivery_old.csv': '../datasets/delivery_time.csv',
    'graphics_old.csv': '../datasets/graphics.csv',
}

# Форматы даты
DATE_FORMAT = {
    'from_service': "%Y-%m-%dT%H:%M:%S",
    'to_service':   "%d.%m.%Y %H:%M:%S"
}

# Процентили для расчета статистики
PERCENTILE = {
    '10percentile':  10,
    '20percentile':  20,
    '30percentile':  30,
    '40percentile':  40,
    '50percentile':  50,
    '60percentile':  60,
    '70percentile':  70,
    '80percentile':  80,
    '90percentile':  90,
    '100percentile': 100,
}

# Логи работы сервиса
LOG_MESSAGES = {
    'start_service':       '\nСтарт работы сервиса DELIVERY TIME STATISTICS:',
    'stop_service':        '\nСтоп работы сервиса DELIVERY TIME STATISTICS:',
    'operating_time':      '\nВремя работы сервиса: %s мин.',
    'separating_line':     '\n' + '-' * 73 + '\n',
    'successful_download': '\tДатасет со сроками доставок успешно загружен...',
    'empty_new_data':      '\tЗа данный период нет новых данных...',
    'send_statistics':     '\tСтатистика по срокам дотавок успешно отправлена...'
}

# Гуид производителя не отправляемый на 1hmm
BAD_GUID = '00000000-0000-0000-0000-000000000000'
