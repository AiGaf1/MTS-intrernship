# MTS-intrernship
## Human detector

Video https://www.youtube.com/watch?v=6ueyBesTxTQ&ab_channel=UcchashSarkar

![ans](https://user-images.githubusercontent.com/33295142/104318277-3c91bb80-54f0-11eb-98c3-95bfb70233c3.gif)



## Wrist detector

Video https://www.youtube.com/watch?v=whZwZ8jeq5E&ab_channel=StarTJ
#### To run the project
```bash
python demo_camera_V2.0.py
```

![resultgirl](https://user-images.githubusercontent.com/33295142/105380064-8bd99980-5c1e-11eb-854d-95ed328f8485.gif)

![result](https://user-images.githubusercontent.com/33295142/105380311-ca6f5400-5c1e-11eb-9855-dc0b24b65313.gif)



After cutting a video program returns all shots in black and white mode.

![frame74](https://user-images.githubusercontent.com/33295142/106120339-532e4880-6167-11eb-92f2-cf0d9798d166.jpg)

### Result

![Peek 2021-02-21 21-45](https://user-images.githubusercontent.com/33295142/118702255-5e43dc00-b81d-11eb-9c64-7807941d878b.gif)

### To run demo_camera_V2.0.py make next steps:

#### Шаг 1. Clone and install all requirements

```bash
$ git clone https://github.com/SyBorg91/pose-estimation-detection
$ cd pose-estimation-detection
$ pip3 install -r requirements.txt
```


#### Шаг 2. Change version tensorflow to 1.13.2
```
$ pip install tensorflow==1.13.2
```

#### Шаг3. Run the program

```
$ python demo_camera_V2.0.py --model=mobilenet_thin --resize=432x368 --camera=0
```


