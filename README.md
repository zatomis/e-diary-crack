# Электронный дневник школы. Добавление похвал

Этот скрипт способен добавлять похвалы для учеников 6а класса. 

## Запуск

- Скачайте скрипт
- Если сервер не запущен - запустите сервер командой `python3 manage.py runserver`
- Необходимо попасть в (InteractiveConsole)
- Чтобы запустить скрипт его нужно целиком “копипастнуть” в shell
- Или произведите импорт скрипта import crack
- Создайте похвалу ученику, например
 ```
crack.create_commendation('Фролов Иван', 'Музыка')
 ```
- Удалить замечания - используйте remove_chastisements('Укажите ФИО')
 ```
crack.remove_chastisements('Укажите ФИО')
 ```
- Исправить оценки 2 и 3 на 5 - используйте change_mark('Укажите ФИО')
 ```
crack.change_mark('Укажите ФИО')
 ```


## Автор
* **Zatomis** - *Цель проекта* - Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org)
