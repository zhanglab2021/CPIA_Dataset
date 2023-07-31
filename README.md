# CPIA_data_process

The CPIA dataset contains 3,474,406 (the total number is growing as we continue to process the datasets) standardized images, covering over 50 organs/tissues and about 98 kinds of diseases, which includes two main data types: whole slide images (WSIs) and characteristic regions of interest (ROIs).

In this repo, we provide relevant codes for processing all sub-datasets within the CPIA dataset. 

<img width="466" alt="image" src="https://github.com/zhanglab2021/CPIA_Dataset/assets/91015667/7b1358ff-591e-4feb-b6a6-d4dfa9210d5f">

*The compositions and WSI processing strategy of the CPIA dataset.*

<img width="254" alt="image" src="https://github.com/zhanglab2021/CPIA_Dataset/assets/91015667/8cc2a2f6-473c-44f5-827a-ea568bd289d2">

*The multi-scale strategy and diverse characteristics of the CPIA dataset.*

## WSI
Each WSI dataset is divided into four levels using one python program. Most of the Whole Slide Imaging (WSI) images are stored in the SVS format, which includes the micron-per-pixel (MPP) information in the header file. Our processing program can automatically identify the MPP of each image and standardize it to 0.4942um/pixel by adjusting the edge length of each patch. Finally, the patch images are divided into four different sizes with edge lengths of 3840, 960, 384, and 96, respectively, and stored in their respective folders.
| Sub-dataset name  | Process Code | Suffix |
|-------------------|--------------|--------|
| CAM16             | CPIA_WSI     | tif    |
| CATCH dataset     | CPIA_WSI     | svs    |
| CMB-CRC           | CPIA_WSI     | svs    |
| CMB-LCA           | CPIA_WSI     | svs    |
| CMB-MEL           | CPIA_WSI     | svs    |
| CPTAC-AML         | CPIA_WSI     | svs    |
| CPTAC-BRCA        | CPIA_WSI     | svs    |
| CPTAC-CCRCC       | CPIA_WSI     | svs    |
| CPTAC-CM          | CPIA_WSI     | svs    |
| CPTAC-COAD        | CPIA_WSI     | svs    |
| CPTAC-HNSCC       | CPIA_WSI     | svs    |
| CPTAC-LSCC        | CPIA_WSI     | svs    |
| CPTAC-LUAD        | CPIA_WSI     | svs    |
| CPTAC-OV          | CPIA_WSI     | svs    |
| CPTAC-PDA         | CPIA_WSI     | svs    |
| CPTAC-SAR         | CPIA_WSI     | svs    |
| CPTAC-UCEC        | CPIA_WSI     | svs    |
| HER2 tumor ROIs   | CPIA_WSI     | svs    |
| MSKCC(SLN-Breast) | CPIA_WSI     | svs    |
| PAIP2019          | CPIA_WSI     | svs    |
| PAIP2020          | CPIA_WSI     | svs    |
| PAIP2021          | CPIA_WSI     | svs    |
| Post-NAT-BRCA     | CPIA_WSI     | svs    |
| TCGA-ACC          | CPIA_WSI     | svs    |
| TCGA-BLCA         | CPIA_WSI     | svs    |
| TCGA-BRCA         | CPIA_WSI     | svs    |
| TCGA-CESC         | CPIA_WSI     | svs    |
| TCGA-CHOL         | CPIA_WSI     | svs    |
| TCGA-COAD         | CPIA_WSI     | svs    |
| TCGA-DLBC         | CPIA_WSI     | svs    |
| TCGA-ESCA         | CPIA_WSI     | svs    |
| TCGA-GBM          | CPIA_WSI     | svs    |
| TCGA-HNSC         | CPIA_WSI     | svs    |
| TCGA-KICH         | CPIA_WSI     | svs    |
| TCGA-KIRC         | CPIA_WSI     | svs    |
| TCGA-KIRP         | CPIA_WSI     | svs    |
| TCGA-LGG          | CPIA_WSI     | svs    |
| TCGA-LIHC         | CPIA_WSI     | svs    |
| TCGA-LUAD         | CPIA_WSI     | svs    |
| TCGA-LUSC         | CPIA_WSI     | svs    |
| TCGA-MESO         | CPIA_WSI     | svs    |
| TCGA-OV           | CPIA_WSI     | svs    |
| TCGA-PAAD         | CPIA_WSI     | svs    |
| TCGA-PCPG         | CPIA_WSI     | svs    |
| TCGA-PRAD         | CPIA_WSI     | svs    |
| TCGA-READ         | CPIA_WSI     | svs    |
| TCGA-SARC         | CPIA_WSI     | svs    |
| TCGA-SKCM         | CPIA_WSI     | svs    |
| TCGA-STAD         | CPIA_WSI     | svs    |
| TCGA-TGCT         | CPIA_WSI     | svs    |
| TCGA-THCA         | CPIA_WSI     | svs    |
| TCGA-THYM         | CPIA_WSI     | svs    |
| TCGA-UCEC         | CPIA_WSI     | svs    |
| TCGA-UCS          | CPIA_WSI     | svs    |
| TCGA-UVM          | CPIA_WSI     | svs    |


## ROI
The processing code for the ROI dataset is related to the structure of the original dataset. After the processing is complete, each dataset folder contains only all images of that dataset, with each image having a dimension of 384x384 pixels, and is stored in jpg format. 

Before processing the data, please ensure that only the target images to be processed are contained in the input path of the program, and enter the correct suffix of the images to be processed (this might require slight adjustments to the original dataset folder).
  
| Sub-dataset name                                     | Process Code                                   | Suffix | Add_class |
|------------------------------------------------------|------------------------------------------------|--------|-----------|
| ANHIR                                                | CPIA_ROI_1_Crop&Resize                         | png    | FALSE     |
| BCSS                                                 | CPIA_ROI_1_Crop&Resize                         | png    | FALSE     |
| AML_Cytomorphology                                   | CPIA_ROI_1_Crop&Resize                         | tiff   | FALSE     |
| BCCD                                                 | CPIA_ROI_1_Crop&Resize                         | jpg    | FALSE     |
| Blood_Cell_Images                                    | CPIA_ROI_1_Crop&Resize                         | jpg    | TRUE      |
| BreakHis                                             | CPIA_ROI_0_BreakHis + CPIA_ROI_1_Crop&Resize   | jpg    | TRUE      |
| Breast_Histopathology_Images                         | CPIA_ROI_1_Crop&Resize                         | png    | FALSE     |
| BreastCancerCells                                    | CPIA_ROI_1_Crop&Resize                         | tif    | FALSE     |
| BreastPathQ                                          | CPIA_ROI_1_Crop&Resize                         | tif    | FALSE     |
| BreCaHAD                                             | CPIA_ROI_1_Crop&Resize                         | tif    | FALSE     |
| Chaoyang                                             | CPIA_ROI_1_Crop&Resize                         | jpg    | FALSE     |
| Colorectal Histology MNIST                           | CPIA_ROI_1_Crop&Resize                         | tif    | FALSE     |
| CoNSeP                                               | CPIA_ROI_1_Crop&Resize                         | png    | FALSE     |
| CRAG                                                 | CPIA_ROI_1_Crop&Resize                         | jpg    | FALSE     |
| CRChistophenotypes                                   | CPIA_ROI_1_Crop&Resize                         | bmp    | FALSE     |
| CRC-TP                                               | CPIA_ROI_1_Crop&Resize                         | png    | TRUE      |
| CRC-VAL-HE-7K                                        | CPIA_ROI_1_Crop&Resize                         | jpg    | FALSE     |
| CryoNuSeg                                            | CPIA_ROI_1_Crop&Resize                         | tif    | FALSE     |
| DataBiox                                             | CPIA_ROI_1_MicroScope DataBiox                 | jpg    | FALSE     |
| GasHisSDB                                            | CPIA_ROI_0_GasHisSDB + CPIA_ROI_1_Crop&Resize  | jpg    | FALSE     |
| Gastrointestinal_Cancer                              | CPIA_ROI_1_Crop&Resize                         | jpg    | FALSE     |
| Gleason 2019                                         | CPIA_ROI_1_Crop&Resize                         | jpg    | FALSE     |
| HuBMAP+HBA_512                                       | CPIA_ROI_1_Crop&Resize                         | png    | FALSE     |
| Kumar(MoNuSeg)                                       | CPIA_ROI_1_Crop&Resize                         | tif    | FALSE     |
| LISC                                                 | CPIA_ROI_1_Crop&Resize                         | bmp    | FALSE     |
| LizardDataset                                        | CPIA_ROI_1_Crop&Resize                         | png    | FALSE     |
| Lung_and_Colon_Cancer_Histopathological_Images_Colon | CPIA_ROI_1_Crop&Resize                         | jpg    | TRUE      |
| Lung_and_Colon_Cancer_Histopathological_Images_Lung  | CPIA_ROI_1_Crop&Resize                         | jpg    | TRUE      |
| LYON19                                               | CPIA_ROI_1_Crop&Resize                         | png    | FALSE     |
| Malignant_Lymphoma_Dataset                           | CPIA_ROI_1_Crop&Resize                         | tif    | FALSE     |
| MARS                                                 | CPIA_ROI_1_Crop&Resize                         | png    | FALSE     |
| MHIST                                                | CPIA_ROI_1_Crop&Resize                         | png    | FALSE     |
| MoNuSAC                                              | CPIA_ROI_1_Crop&Resize                         | tif    | FALSE     |
| Monuseg_train&test                                   | CPIA_ROI_1_Crop&Resize                         | png    | FALSE     |
| Naylor et al, IEEE TMI 2019                          | CPIA_ROI_1_Crop&Resize                         | png    | FALSE     |
| NCT-CRC-HE-100K                                      | CPIA_ROI_1_Crop&Resize                         | tif    | FALSE     |
| Osteosarcoma_Tumor_Assessment                        | CPIA_ROI_1_Crop&Resize                         | jpg    | FALSE     |
| P_falciparum                                         | CPIA_ROI_1_MicroScope P.falciparum             | jpg    | FALSE     |
| P_uninfected                                         | CPIA_ROI_1_MicroScope P.uninfected             | jpg    | FALSE     |
| P_vivax                                              | CPIA_ROI_1_MicroScope P.vivax                  | jpg    | FALSE     |
| PCam                                                 | CPIA_ROI_1_Crop&Resize                         | tif    | FALSE     |
| pRCC                                                 | CPIA_ROI_1_Crop&Resize                         | jpg    | FALSE     |
| SICAPv2                                              | CPIA_ROI_1_Crop&Resize                         | jpg    | FALSE     |
| SIPaKMeD                                             | CPIA_ROI_0_SIPaKMeD + CPIA_ROI_1_Crop&Resize   | jpg    | FALSE     |
| warwick_CLS                                          | CPIA_ROI_0_Warwick + CPIA_ROI_1_Crop&Resize    | jpg    | FALSE     |
| WBC                                                  | CPIA_ROI_1_Crop&Resize                         | jpg    | TRUE      |
| Weinart et al, Scientific Reports 2012               | CPIA_ROI_1_Crop&Resize                         | jpg    | FALSE     |
| WSSS4LUAD                                            | CPIA_ROI_1_Crop&Resize                         | png    | TRUE      |
