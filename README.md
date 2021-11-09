# Spectrum52 version 1.0
Это программа для сравнения фотографий двух линейчатых спектров.
Конкретно в этой программе в качестве примера используются фотографии эмиссионного 
спектра железеза, полученные в ходе выполнения лабораторной работы со спектрографом.
Они сравниваются с обработанным изображением из методического пособия(повышенна контрастность
и инвертированны цвета) файл под названием Risunok.
Для увеличения точности графика интенсивности линий, в программе есть функция upscale prototype,
которая увеличивает размер второй фотографии относительно первой, чтобы можно было более точно определить длинны волн.


В этой проге могут возникнуть проблемы в кодировке (Будет выдавать ошибку при выборе
файла в названии которого или в названии его пути будет кириллица)
Это решается следующим способом:
Во первых, проверяем открыли ли мы код с помощью Pycharm(если нет, бегом качать) 
вот ссылка: https://www.jetbrains.com/ru-ru/pycharm/download/#section=windows
(Качаем Community для разработки только на Python)
Во вторых, нажимаем file, делаем всё как показанно на инструкции(чтобы поменять кодировку на ту, кторая переваривает кириллицу)
![Image alt](https://github.com/KrechkoVsevolod201/Spectrum52/raw/master/Screenshots/img.png)
![Image alt](https://github.com/KrechkoVsevolod201/Spectrum52/raw/master/Screenshots/img_1.png)
![Image alt](https://github.com/KrechkoVsevolod201/Spectrum52/raw/master/Screenshots/img_2.png)
![Image alt](https://github.com/KrechkoVsevolod201/Spectrum52/raw/master/Screenshots/img_3.png)
![Image alt](https://github.com/KrechkoVsevolod201/Spectrum52/raw/master/Screenshots/img_4.png)

Когда все этапы прошли, запускаем gui.py
У вас вылетит такая программа:
![Image alt](https://github.com/KrechkoVsevolod201/Spectrum52/raw/master/Screenshots/img_5.png)

Если не понятно, лезем в Help, там есть подсказки


Как делать градуировочный граффик?

1) открываем файлик exel из папки HelpFiles
2) Там будут записанны значения длин волн в соответствии с фотографиями спектра
3) Запускаем программу и выбирааем первый файл - фото спектра, а второй фото из атласа файл Risunok_59.jpg
   
   ![Image alt](https://github.com/KrechkoVsevolod201/Spectrum52/raw/master/Screenshots/img_6.png)
   ![Image alt](https://github.com/KrechkoVsevolod201/Spectrum52/raw/master/Screenshots/img_7.png)
4) Наводим курсор на указанные точки на фото и в правом нижнем углу записываем координату х, которая будет соответствовать нужной нам длине волны
   ![Image alt](https://github.com/KrechkoVsevolod201/Spectrum52/raw/master/Screenshots/img_8.png)

5) строим на основе координат х и длин волн из файлика граффик

Дальше будет часть с вольфрамом, дополню позже