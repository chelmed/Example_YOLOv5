# Example_YOLOv5
Пример обучения YOLOv5.

Цель: запустить обучение YOLOv5. Датасет взят с соревнования kaggle: https://www.kaggle.com/c/nfl-health-and-safety-helmet-assignment/data. 
Таргет представлен пятью классами с большим дисбалансом, но в основном это дектеция шлемов.   

Полность реализацию можно посмотреть на Google Colab: 
 [![Open In Colab](https://github.com/chelmed/Example_YOLOv5/blob/main/colab.svg)](https://colab.research.google.com/drive/19GyzEbl21rQ2Mzs7eGF2cUOs3EMX10UN?usp=sharing)

YOLOv5 в отличие от других версий, реализована на Pytorch (в основе также имеет архитектуру darknet).

Реализация: 

1) Необходимо в директории проекта создать следующую струтуру:<br/> 
![demo](https://github.com/chelmed/Example_YOLOv5/blob/main/str_dir.png)<br/> 
!в txt класс, позиция центра bb, высота и ширина bb в относительных координатах. 
2) Создать файл формата yaml (как пример Create.yaml)

Инференс на видео:<br/>
Видео до:<br/>
![caption](https://github.com/chelmed/Example_YOLOv5/blob/main/video.gif)<br/> 
Видео после:<br/> 
![caption](https://github.com/chelmed/Example_YOLOv5/blob/main/detected_video.gif)<br/> 
