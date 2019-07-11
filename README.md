# db-hack

## Описание

С помощью данного скрипта можно изменить все свои двойки и тройки на 4,5. Удалить все негативные замечания. Добавить похвалу.

## Как использовать

1. Развернуть сайт с [электронным дневником](https://github.com/devmanorg/e-diary.git)

2. Открыть shell проекта

```sh
python manage.py shell
```

3. Скопировать содержимое scripts.py в shell

4. Получить ученика

```python
schoolkid = get_schoolkid(schoolkid_name) # получить ученика
```

5. Вызвать нужную функцию

```python

fix_marks(schoolkid)  # исправить оценки

remove_сhastisements(schoolkid)  # удалить замечания

make_commendation(schoolkid, subject) # создать похвалу
```

![Alt](http://ipic.su/img/img7/fs/orm3.1562416322.gif)
