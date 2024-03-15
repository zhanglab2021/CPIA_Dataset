# CPIA_Dataset

The CPIA dataset contains 148,962,586 standardized images, covering over 48 organs/tissues and about 100 kinds of diseases, which includes two main data types: whole slide images (WSIs) and characteristic regions of interest (ROIs).

In this repo, we provide relevant codes for processing all sub-datasets within the CPIA dataset. 

<img width="1039" alt="image" src="https://github.com/zhanglab2021/CPIA_Dataset/assets/91015667/8c4bcb8a-ab11-4aaf-b6bc-7ccf49231801">

*The compositions and WSI processing strategy of the CPIA dataset.*

<img width="729" alt="image" src="https://github.com/zhanglab2021/CPIA_Dataset/assets/91015667/341747a7-3b98-490f-b1f2-2e09ac1ef039">

*The multi-scale strategy and diverse characteristics of the CPIA dataset.*


# CPIA-Mini

The CPIA-Mini dataset is a lightweight and categorically balanced CPIA fraction. 
In this dataset, sample number ratio of XL, L, M, and S is around 1:16:32:32.

The CPIA-Mini dataset can be downloaded at:

BaiduDisk: https://pan.baidu.com/s/1alRuGmxa7fXQRhTiOlfKrw  Password: 9ub9

GoogleDrive: https://drive.google.com/drive/folders/1tCruBcWnADJTChgXgnOJSQLxIoroYoWD?usp=sharing

<img width="1076" alt="image" src="https://github.com/zhanglab2021/CPIA_Dataset/assets/91015667/b783e21c-c67e-4ceb-a1d8-e6b5294e7481">

*The CPIA-Mini dataset construction framework.*


## Usage

The CPIA-Mini dataset is stored in a .zip archive format. After downloading the CPIA_Mini dataset in to your [CPIA directory], researchers can use the bash script 'nohup bash build_cpia_mini.sh &' at [CPIA directory] to unzip the dataset in a Linux operating system and use the dataset as needed.

After the building process, In [CPIA directory], there will be four folders: L,M,S,All correspingding to the multi-scale CPIA-mini subset and the total CPIA-mini dataset.
