---
# Front matter
lang: ru-RU
title: "Лабораторная работа №1"
author: "Роман Владимирович Иванов"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Вспомнить, как работать с git и познакомиться с возможностями разметки Markdown.

# Задание

1. Создание репозитория.
2. Создание коммитов и загрузка файлов.
3. Создание ключей.
4. Подготовка отчета в формате .pdf и .docx.
5. Подготовка презентации в формате .pdf.
6. Создать релиз.

# Выполнение лабораторной работы

Создал папку с проектом и инициализировал репозиторий. (рис. 1)

![Новая папка с проектом](image/1.png){ рис. 1 }

Произвел коммит и загрузил все файлы (рис. 2)

![Загрузка файлов](image/2.png){ рис. 2 }

Создал SSH - ключ. (рис. 3-4)

![Создание ключа](image/3.png){ рис. 3 }

![Ключ на github](image/4.png){ рис. 4 }

Подготовил отчет в форматах .md и .docx (рис. 5)

![Компиляция Makefile](image/5.png){ рис. 5 }

![Подготовка отчета](image/6.png){ рис. 6 }

Подготовил презентацию в формате .md

![Подготовка ghtptynfwbb](image/7.png){ рис. 7 }

![Компиляция Makefile](image/8.png){ рис. 8 }

Создал релиз

![Релиз](image/9.png){ рис. 9 }

# Выводы

Вспомнил, как работать c git. Научился работать с Markdown.
