# MTS-intrernship
A Human detector

Видео взял отсюда https://www.youtube.com/watch?v=6ueyBesTxTQ&ab_channel=UcchashSarkar

![ans](https://user-images.githubusercontent.com/33295142/104318277-3c91bb80-54f0-11eb-98c3-95bfb70233c3.gif)

# A left wrist detector

Видео взял отсюда https://www.youtube.com/watch?v=whZwZ8jeq5E&ab_channel=StarTJ
#### Чтобы запустит файл нужно запустить через терминал и ввести

python detect_wrist.py --input "path to video"

![resultgirl](https://user-images.githubusercontent.com/33295142/105380064-8bd99980-5c1e-11eb-854d-95ed328f8485.gif)

![result](https://user-images.githubusercontent.com/33295142/105380311-ca6f5400-5c1e-11eb-9855-dc0b24b65313.gif)



После обрезки видео программа выводит все кадры в черно-белые фото

![frame74](https://user-images.githubusercontent.com/33295142/106120339-532e4880-6167-11eb-92f2-cf0d9798d166.jpg)

## Новая версия 
### Чтобы запустить demo_camera_V2.0.py нужно склонировать библиотеку с другого репозитория

### Клонирование и  установка зависимостей

```bash
$ git clone https://github.com/SyBorg91/pose-estimation-detection
$ cd pose-estimation-detection
$ pip3 install -r requirements.txt
```

### Запустить программы

```
$ python run_webcam.py --model=mobilenet_thin --resize=432x368 --camera=0
```



