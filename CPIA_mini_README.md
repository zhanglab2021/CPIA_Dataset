# CPIA_Mini

The CPIA-Mini dataset is a lightweight and categorically balanced CPIA fraction. 
In this dataset, sample number ratio of XL, L, M, and S is around 1:16:32:32.

The CPIA_Mini dataset can be downloaded at:

BaiduDisk: https://pan.baidu.com/s/1alRuGmxa7fXQRhTiOlfKrw  Password: 9ub9

<img width="1076" alt="image" src="https://github.com/zhanglab2021/CPIA_Dataset/assets/91015667/b783e21c-c67e-4ceb-a1d8-e6b5294e7481">

*The CPIA-Mini dataset construction framework.*


## Usage

The CPIA_Mini dataset is stored in a .zip archive format. After downloading the CPIA_Mini dataset, researchers can use the following code to unzip the dataset in a Linux operating system and use the dataset as needed.

zip -F L.zip --out L_Scale.zip

zip -FF L_Scale.zip --out L.zip -fz

zip -F M.zip --out M_Scale.zip

zip -FF M_Scale.zip --out M.zip -fz


rm -f L_Scale.zip

rm -f L.z01

rm -f M_Scale.zip

rm -f M.z01

rm -f M.z02


mv L.zip datasets

mv M.zip datasets

mv S.zip datasets


cd datasets/path

unzip L.zip

unzip M.zip

unzip S.zip


rm -f L.zip

rm -f M.zip

rm -f S.zip


mkdir All

cp -r L/* All/ &

cp -r M/* All/ &

cp -r S/* All/ &
