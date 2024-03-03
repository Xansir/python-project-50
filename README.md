### Hexlet tests and Python CI status:
[![hexlet-check](https://github.com/Xansir/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Xansir/python-project-50/actions/workflows/hexlet-check.yml)
[![Python CI](https://github.com/Xansir/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Xansir/python-project-50/actions/workflows/pyci.yml)

### Code Climate Maintainability & Test Coverage
[![Maintainability](https://api.codeclimate.com/v1/badges/eb044d7d27aab9fce340/maintainability)](https://codeclimate.com/github/Xansir/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/eb044d7d27aab9fce340/test_coverage)](https://codeclimate.com/github/Xansir/python-project-50/test_coverage)

## Описание
Небольшая CLI-утилита для вывода различий между двумя json/yaml файлами

## Установка
_Требования для установки:_
- _python = "^3.10"_
- _poetry = "^1.2.2"_
- _Чтобы работать с проектом, вам необходимо клонировать репозиторий на свой компьютер.
```bash
#HTTPS
>> git clone https://github.com/Xansir/python-project-50.git
#SSH
>> git clone git@github.com:Xansir/python-project-50.git
```
_Осталось перейти в нужную директорию и установить пакет:_
```bash
>> cd python-project-50
>> make install
>> make build
>> make publish
>> make package-install
# _Если раннее установка уже проводилась - чтобы обновить сборку нужно ввести комманду:
# >> make package-reinstall
```
## Основные команды
- gendiff -h Выводит пользователю основной функционал программы.
- gendiff filepath1.json/yml filepath2.json/yml Выводит представление разницы файлов в стандартном для программы формате.
- genidff -f plain filepath1.json/yml filepath2.json/yml Выводит представление разницы файлов в плоском формате.
- genidff -f json filepath1.json/yml filepath2.json/yml Выводит представление разницы файлов в JSON формате.


## Plain 
[![asciicast](https://asciinema.org/a/t1YVHWYtZhJ5afYfODNj9Djcg.svg)](https://asciinema.org/a/t1YVHWYtZhJ5afYfODNj9Djcg)


## Stylish
[![asciicast](https://asciinema.org/a/xWThFvZRoYEwnF33LbHl3fKaS.svg)](https://asciinema.org/a/xWThFvZRoYEwnF33LbHl3fKaS)

## Json
[![asciicast](https://asciinema.org/a/v4Onz3BzrCAkhDSGNxo8ZQopf.svg)](https://asciinema.org/a/v4Onz3BzrCAkhDSGNxo8ZQopf)
