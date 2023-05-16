# 010-painter 1.0.2
🤖 Программа для автоматизации визуализации временной диаграммы логической схемы

## Начало работы
Перед первым запуском программы необходимо установить зависимости из `requirements.txt` \
`pip install -r requirements.txt` 

## Использование
Программа ожидает на вход путь до форматированного файла, передать который можно через консоль
`"010 painter.pyw" path_fo_file.txt`
или перетащив сам файл на иконку срипта (исполняемого файла)

## Формат данных
Программа принимает на вход путь до файла с формтированными данными в качестве параметра запуска.
> Пример содержимого входного файла и результата выполнения
> 
> <code>10 10 10 10 name=C
> 11 00 00 00 name=R
> 00 11 00 00 name=S
> 00 01 11 11 name=Q color=green
> 11 10 00 00 name=!Q color=red
> </code>
>
> ![изображение](https://user-images.githubusercontent.com/47332822/236255185-3e99403f-4a31-470b-86f6-9bb46418cb3c.png)

В текущей версии программы существуют следующие правила к оформлению входных данных:
* каждая строчка файла является набором данных для отдельной оси
* в каждом наборе данных должны присутствовать по два логических значения (0 или 1) на один такт
* кол-во тактов должно совпадать в каждом наборе

## Исполняемый файл
❗️ 010 painter.exe может определяться антивирусными средствами как вредоносное ПО, в частности, Microsoft Defender определяет exe как Trojan:Win32/Wacatac.H!ml.
Если вы сомневаетесь в безвредности собранного исполняемого файла, предлагаю вам собрать его самостоятельно, предварительно установив `pyinstaller` и запустив `build.bat`,
или просто запускать скрипт `010 painter.pyw`. <br>
<br>
Причина ложного детектирования кроется в частом использовании `pyinstaller` для сокрытия вредоносного кода. 

## Поддерживаемые платформы
На данный момент поддерживаются Windows и Linux.