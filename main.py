import json  # импортируем модуль json для работы с json файлами
# запрашиваем у пользователя номер квалификации
qualification_number = input("Введите номер квалификации: ")
# создаем пустой список для результатов поиска
results = []
# открываем файл и обрабатываем его построчно
try:
    with open('dump.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  # загружаем данные из файла в переменную data
        print("Файл успешно загружен.")
        # проходим по всем элементам данных
        for item in data:
            if isinstance(item, dict):  # проверяем, что элемент является словарем
                model = item.get('model', 'нет модели')  # получаем значение ключа 'model'
                fields = item.get('fields', {})  # получаем значение ключа 'fields'
                # проверяем, что модель - data.skill или data.specialty
                if model in ['data.skill', 'data.specialty']:
                    code = fields.get('code', 'нет кода')  # получаем значение ключа 'code'
                    title = fields.get('title', 'нет названия')  # получаем значение ключа 'title'
                    desc = fields.get('desc', 'нет описания')  # получаем значение ключа 'desc'
                    # проверяем, если номер квалификации присутствует в коде
                    if qualification_number in code:
                        results.append({
                            "model": model,
                            "code": code,
                            "title": title,
                            "desc": desc
                        })
                        print(f"Найден элемент: {item}")  # отладочный вывод
except FileNotFoundError:
    print("Ошибка: файл dump.json не найден.")
    exit()
except json.JSONDecodeError:
    print("Ошибка: не удалось декодировать json.")
    exit()
# выводим результаты
if results:
    print("=============== Найдено ===============")
    for qual in results:
        if qual['model'] == 'data.skill':
            print(f"{qual['code']} >> Квалификация \"{qual['title']}\"")
        elif qual['model'] == 'data.specialty':
            print(f"{qual['code']} >> Специальность \"{qual['title']}\", ПТО")
else:
    print("=============== Не найдено ===============")