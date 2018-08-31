SguExtLO

Description RU:

Преобразователь частоты R&S®SGU100A позволяет расширить диапазон частот с 12 ГГц до 20 или 40 ГГц, при условии
подачи на его вход ВЧ-сигнала в диапазоне от 10 МГц до 12,75 ГГц. Преобразователь имеет 2 варианта исполнения – аналоговая
и векторная версия. В качестве источника немодулированных (CW) сигналов могут выступать аналоговые генераторы
(например SMB-B112 или SMF-B122), а для генерации векторных сигналов дополнительно потребуется еще и внешний
источник I/Q модуляции. При использовании для этих целей генератора AFQ100B полоса модуляции составит до 528 МГц.
Для обеспечения большей полосы – можно воспользоваться генераторами сторонних производителей, в этом случае, на
частотах выше 12 ГГц, внутренний I/Q-модулятор преобразователя способен обеспечить полосу модуляции до 2 ГГц.
Но наилучшим вариантом использования преобразователя будет – совместная работа с генератором R&S®SGS100A.
Объединение этих приборов обеспечивает наименьший форм-фактор на рынке для векторной генерации сигналов в
диапазоне до 20 или 40 ГГц. При размещении их в 19-дюймовой измерительной стойке, они займут либо половину ширины
полки высотой 2U, либо 1U высоты и всю ширину полки. Если требуется разместить приборы на рабочем столе, можно
воспользоваться специальным набором для подключения SGU-Z4, содержащим необходимые кабели и механический
крепеж для передней и задней панелей. Объединенные приборы работают как один инструмент, автоматически
распределяя задачи между собой (один ВЧ-выход для всего диапазона и одни аналоговые I/Q-входы для внешнего модулирующего
сигнала). Вместе они обеспечивают частотный диапазон от 10 МГц до 20 или 40 ГГц без модуляции (CW-режим) и
от 80 МГц до 20 или 40 ГГц с векторной модуляцией (I/Q-режим). Управление связкой приборов осуществляется по интерфейсам
USB, LAN или PCIe посредством программного приложения R&S®SGMA-GUI, устанавливаемого на внешнем ПК. На панели
управления графического интерфейса преобразователь SGU отображается в виде расширения генератора SGS.

Данный скрипт демонстрирует принцип управления преобразователем частоты R&S®SGU100A.

Description EN:

The R&S®SGU100A SGMA Upconverter offers a frequency extension to 40 GHz. When the R&S®SGS100A and the R&S®SGU100A 
are connected, they act as a single instrument for both remote control and manual operation via the R&S®SGMA-GUI 
PC software. The combined instruments offer the same connections as the R&S®SGS100A itself: one RF output for the 
entire frequency range and one analog I/Q input for vector modulation. In this setup, tasks are spread automatically 
and transparently between the two instruments so that users feel as if they are operating one instrument instead of two. 
Equipped with the R&S®SGU100A, the R&S®SGS100A covers the entire frequency range from 10 MHz to 40 GHz without 
modulation, and from 80 MHz to 40 GHz with Vector modulation.

Thisi Python script is an axample how to use external LO with R&S®SGU100A upconverter in remote control mode.

Полное описание на странице продукта:
Detailed description at product page:

https://www.rohde-schwarz.com/product/sgu100a-productstartpage_63493-60676.html