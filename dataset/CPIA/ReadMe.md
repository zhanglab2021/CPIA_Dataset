# CPIA Details&Summary
In order to facilitate users to use the CPIA dataset, we prepared two tables to show the details. The two tables are respectively CPIA_summary.xlsx and CPIA_details.xlsx. The use of each folder is described in detail below:

## CPIA_summary.xlsx
The table divides the data into two categories: WSI and ROI. And this table gives a detailed description of the information in each sub-dataset.

### [Sub-dataset name]
This column is the name of the processed sub-datasets under the CPIA framework, and the corresponding datasets compression package can be found according to the information in this column.

### [Original name]
This column is the original name of the initial publication of the sub-datasets.
### [Organ/tissue]
This column lists organ/tissue categories covered by pathological images in different sub-datasets. Researchers can find processed sub-datasets of specified categories according to their needs. Some sub-datasets contain pathological images of multiple organs.
### [Disease]
This column lists disease categories in pathological images in different sub-datasets. Some sub-datasets contain pathological images of multiple disease categories.
### [Total number]
This column is the number of processed samples in the CPIA sub-datasets.
### [Storage]
Due to the large-scale feature of the CPIA dataset, we store CPIA in nine links under the SicenceDB. This column is the storage number where the different sub-datasets are located. The user can find the corresponding complete sub-dataset in the specified link.
### [Dyeing method]
This column is the dyeing methods for pathological images in different sub-datasets.
### [Field]
This column divides the sub-datasets into histopathology and cytopathology.
### [Time] 
This column lists the year each dataset was published.
### [Dataset linking]
This column is the download links of the original datasets. Users can follow the links to find more detailed descriptions and information about the original datasets.
### [Related literatures or acknowledgement]
This column are the original articles or web of the sub-datasets. Because the number of articles is too large, these articles are not directly quoted in our paper, but are organized in this table.


## CPIA_details.xlsx
This table consists of three sheets in total. This corresponds to the three scales of the CPIA dataset: L, M, and S. The user can find the name of the sub-dataset and the number of samples at that scale in the corresponding sheet.
### L Scale
| Data type | Sub-dataset name                  | Original name                                             | Number   |
|-----------|-----------------------------------|-----------------------------------------------------------|----------|
| WSIs      | CAM16-3840                        | Camelyon16                                                | 3122     |
|           | CAM16-960                         | Camelyon16                                                | 43249    |
|           | CATCH dataset-3840                | CATCH                                                     | 14496    |
|           | CATCH dataset-960                 | CATCH                                                     | 224126   |
|           | CMB-CRC-3840                      | CMB-CRC                                                   | 257      |
|           | CMB-CRC-960                       | CMB-CRC                                                   | 3861     |
|           | CMB-LCA-3840                      | CMB-LCA                                                   | 41       |
|           | CMB-LCA-960                       | CMB-LCA                                                   | 594      |
|           | CMB-MEL-3840                      | CMB-MEL                                                   | 657      |
|           | CMB-MEL-960                       | CMB-MEL                                                   | 9910     |
|           | CPTAC-AML-3840                    | CPTAC-AML                                                 | 902      |
|           | CPTAC-AML-960                     | CPTAC-AML                                                 | 14365    |
|           | CPTAC-BRCA-3840                   | CPTAC-BRCA                                                | 6781     |
|           | CPTAC-BRCA-960                    | CPTAC-BRCA                                                | 103681   |
|           | CPTAC-CCRCC-3840                  | CPTAC-CCRCC                                               | 6885     |
|           | CPTAC-CCRCC-960                   | CPTAC-CCRCC                                               | 102574   |
|           | CPTAC-CM-3840                     | CPTAC-CM                                                  | 2580     |
|           | CPTAC-CM-960                      | CPTAC-CM                                                  | 37811    |
|           | CPTAC-COAD-3840                   | CPTAC-COAD                                                | 4507     |
|           | CPTAC-COAD-960                    | CPTAC-COAD                                                | 70044    |
|           | CPTAC-HNSCC-3840                  | CPTAC-HNSCC                                               | 6037     |
|           | CPTAC-HNSCC-960                   | CPTAC-HNSCC                                               | 84905    |
|           | CPTAC-LSCC-3840                   | CPTAC-LSCC                                                | 6035     |
|           | CPTAC-LSCC-960                    | CPTAC-LSCC                                                | 90359    |
|           | CPTAC-LUAD-3840                   | CPTAC-LUAD                                                | 26932    |
|           | CPTAC-LUAD-960                    | CPTAC-LUAD                                                | 411948   |
|           | CPTAC-OV-3840                     | CPTAC-OV                                                  | 2031     |
|           | CPTAC-OV-960                      | CPTAC-OV                                                  | 31656    |
|           | CPTAC-PDA-3840                    | CPTAC-PDA                                                 | 4536     |
|           | CPTAC-PDA-960                     | CPTAC-PDA                                                 | 63840    |
|           | CPTAC-SAR-3840                    | CPTAC-SAR                                                 | 4034     |
|           | CPTAC-SAR-960                     | CPTAC-SAR                                                 | 59700    |
|           | CPTAC-UCEC-3840                   | CPTAC-UCEC                                                | 8727     |
|           | CPTAC-UCEC-960                    | CPTAC-UCEC                                                | 126032   |
|           | HER2 tumor ROIs-3840              | HER2 tumor ROIs                                           | 1025     |
|           | HER2 tumor ROIs-960               | HER2 tumor ROIs                                           | 13400    |
|           | MSKCC(SLN-Breast)-3840            | MSKCC(SLN-Breast)                                         | 1434     |
|           | MSKCC(SLN-Breast)-960             | MSKCC(SLN-Breast)                                         | 21709    |
|           | PAIP2019-3840                     | PAIP2019                                                  | 4321     |
|           | PAIP2019-960                      | PAIP2019                                                  | 67556    |
|           | PAIP2020-3840                     | PAIP2020                                                  | 3042     |
|           | PAIP2020-960                      | PAIP2020                                                  | 47543    |
|           | PAIP2021-3840                     | PAIP2021                                                  | 13295    |
|           | PAIP2021-960                      | PAIP2021                                                  | 208282   |
|           | Post-NAT-BRCA-3840                | Post-NAT-BRCA                                             | 1222     |
|           | Post-NAT-BRCA-960                 | Post-NAT-BRCA                                             | 18931    |
|           | TCGA-ACC-3840                     | TCGA-ACC                                                  | 14739    |
|           | TCGA-ACC-960                      | TCGA-ACC                                                  | 229090   |
|           | TCGA-BLCA-3840                    | TCGA-BLCA                                                 | 27318    |
|           | TCGA-BLCA-960                     | TCGA-BLCA                                                 | 415820   |
|           | TCGA-BRCA-3840                    | TCGA-BRCA                                                 | 45956    |
|           | TCGA-BRCA-960                     | TCGA-BRCA                                                 | 695826   |
|           | TCGA-CESC-3840                    | TCGA-CESC                                                 | 10571    |
|           | TCGA-CESC-960                     | TCGA-CESC                                                 | 159682   |
|           | TCGA-CHOL-3840                    | TCGA-CHOL                                                 | 3422     |
|           | TCGA-CHOL-960                     | TCGA-CHOL                                                 | 52151    |
|           | TCGA-COAD-3840                    | TCGA-COAD                                                 | 17932    |
|           | TCGA-COAD-960                     | TCGA-COAD                                                 | 274546   |
|           | TCGA-DLBC-3840                    | TCGA-DLBC                                                 | 1911     |
|           | TCGA-DLBC-960                     | TCGA-DLBC                                                 | 29057    |
|           | TCGA-ESCA-3840                    | TCGA-ESCA                                                 | 7358     |
|           | TCGA-ESCA-960                     | TCGA-ESCA                                                 | 112834   |
|           | TCGA-GBM-3840                     | TCGA-GBM                                                  | 34048    |
|           | TCGA-GBM-960                      | TCGA-GBM                                                  | 510982   |
|           | TCGA-HNSC-3840                    | TCGA-HNSC                                                 | 18938    |
|           | TCGA-HNSC-960                     | TCGA-HNSC                                                 | 289358   |
|           | TCGA-KICH-3840                    | TCGA-KICH                                                 | 9008     |
|           | TCGA-KICH-960                     | TCGA-KICH                                                 | 139803   |
|           | TCGA-KIRC-3840                    | TCGA-KIRC                                                 | 41784    |
|           | TCGA-KIRC-960                     | TCGA-KIRC                                                 | 644506   |
|           | TCGA-KIRP-3840                    | TCGA-KIRP                                                 | 16266    |
|           | TCGA-KIRP-960                     | TCGA-KIRP                                                 | 249601   |
|           | TCGA-LGG-3840                     | TCGA-LGG                                                  | 32739    |
|           | TCGA-LGG-960                      | TCGA-LGG                                                  | 486245   |
|           | TCGA-LIHC-3840                    | TCGA-LIHC                                                 | 22153    |
|           | TCGA-LIHC-960                     | TCGA-LIHC                                                 | 339874   |
|           | TCGA-LUAD-3840                    | TCGA-LUAD                                                 | 28979    |
|           | TCGA-LUAD-960                     | TCGA-LUAD                                                 | 446166   |
|           | TCGA-LUSC-3840                    | TCGA-LUSC                                                 | 29561    |
|           | TCGA-LUSC-960                     | TCGA-LUSC                                                 | 452919   |
|           | TCGA-MESO-3840                    | TCGA-MESO                                                 | 3159     |
|           | TCGA-MESO-960                     | TCGA-MESO                                                 | 47365    |
|           | TCGA-OV-3840                      | TCGA-OV                                                   | 21955    |
|           | TCGA-OV-960                       | TCGA-OV                                                   | 332731   |
|           | TCGA-PAAD-3840                    | TCGA-PAAD                                                 | 9922     |
|           | TCGA-PAAD-960                     | TCGA-PAAD                                                 | 152003   |
|           | TCGA-PCPG-3840                    | TCGA-PCPG                                                 | 11739    |
|           | TCGA-PCPG-960                     | TCGA-PCPG                                                 | 179624   |
|           | TCGA-PRAD-3840                    | TCGA-PRAD                                                 | 24621    |
|           | TCGA-PRAD-960                     | TCGA-PRAD                                                 | 378173   |
|           | TCGA-READ-3840                    | TCGA-READ                                                 | 5668     |
|           | TCGA-READ-960                     | TCGA-READ                                                 | 86539    |
|           | TCGA-SARC-3840                    | TCGA-SARC                                                 | 30394    |
|           | TCGA-SARC-960                     | TCGA-SARC                                                 | 471319   |
|           | TCGA-SKCM-3840                    | TCGA-SKCM                                                 | 22329    |
|           | TCGA-SKCM-960                     | TCGA-SKCM                                                 | 343365   |
|           | TCGA-STAD-3840                    | TCGA-STAD                                                 | 26169    |
|           | TCGA-STAD-960                     | TCGA-STAD                                                 | 404339   |
|           | TCGA-TGCT-3840                    | TCGA-TGCT                                                 | 11512    |
|           | TCGA-TGCT-960                     | TCGA-TGCT                                                 | 181855   |
|           | TCGA-THCA-3840                    | TCGA-THCA                                                 | 29370    |
|           | TCGA-THCA-960                     | TCGA-THCA                                                 | 447596   |
|           | TCGA-THYM-3840                    | TCGA-THYM                                                 | 8693     |
|           | TCGA-THYM-960                     | TCGA-THYM                                                 | 134962   |
|           | TCGA-UCEC-3840                    | TCGA-UCEC                                                 | 38767    |
|           | TCGA-UCEC-960                     | TCGA-UCEC                                                 | 597051   |
|           | TCGA-UCS-3840                     | TCGA-UCS                                                  | 4883     |
|           | TCGA-UCS-960                      | TCGA-UCS                                                  | 75101    |
|           | TCGA-UVM-3840                     | TCGA-UVM                                                  | 1956     |
|           | TCGA-UVM-960                      | TCGA-UVM                                                  | 29376    |
| ROIs      | ANHIR                             | ANHIR                                                     | 80       |
|           | BCSS                              | BCSS                                                      | 151      |
|           | BreaKHis_40x                      | BreakHis                                                  | 1995     |
|           | Breast_Histopathology_Images      | Breast Histopathology Images                              | 277524   |
|           | Colorectal Histology MNIST_Larger | Colorectal Histology MNIST                                | 10       |
|           | CRAG                              | CRAG                                                      | 213      |
|           | DataBiox_4x_10x                   | DataBiox                                                  | 191      |
|           | Gleason 2019                      | Gleason 2019                                              | 331      |
|           | LYON19                            | LYON19                                                    | 441      |
|           | Malignant_Lymphoma_Dataset        | Malignant lymphoma datasets                               | 374      |
|           | MARS                              | MARS                                                      | 1770     |
|           | MHIST                             | MHIST: A Minimalist Histopathology Image Analysis Dataset | 3152     |
|           | Osteosarcoma_Tumor_Assessment     | Osteosarcoma Tumor Assessment                             | 1144     |
|           | warwick_CLS                       | Warwick_QU_dataset                                        | 165      |
| Total     |                                   |                                                           | 12270195 |

### M Scale
| Data type | Sub-dataset name                                     | Original name                                        | Number   |
|-----------|------------------------------------------------------|------------------------------------------------------|----------|
| WSIs      | CAM16-384                                            | Camelyon16                                           | 258703   |
|           | CATCH dataset-384                                    | CATCH                                                | 1379716  |
|           | CMB-CRC-384                                          | CMB-CRC                                              | 23487    |
|           | CMB-LCA-384                                          | CMB-LCA                                              | 3598     |
|           | CMB-MEL-384                                          | CMB-MEL                                              | 60562    |
|           | CPTAC-AML-384                                        | CPTAC-AML                                            | 89605    |
|           | CPTAC-BRCA-384                                       | CPTAC-BRCA                                           | 635265   |
|           | CPTAC-CCRCC-384                                      | CPTAC-CCRCC                                          | 624799   |
|           | CPTAC-CM-384                                         | CPTAC-CM                                             | 229508   |
|           | CPTAC-COAD-384                                       | CPTAC-COAD                                           | 431018   |
|           | CPTAC-HNSCC-384                                      | CPTAC-HNSCC                                          | 511221   |
|           | CPTAC-LSCC-384                                       | CPTAC-LSCC                                           | 548888   |
|           | CPTAC-LUAD-384                                       | CPTAC-LUAD                                           | 2525537  |
|           | CPTAC-OV-384                                         | CPTAC-OV                                             | 194644   |
|           | CPTAC-PDA-384                                        | CPTAC-PDA                                            | 384419   |
|           | CPTAC-SAR-384                                        | CPTAC-SAR                                            | 362956   |
|           | CPTAC-UCEC-384                                       | CPTAC-UCEC                                           | 759724   |
|           | HER2 tumor ROIs-384                                  | HER2 tumor ROIs                                      | 79197    |
|           | MSKCC(SLN-Breast)-384                                | MSKCC(SLN-Breast)                                    | 131736   |
|           | PAIP2019-384                                         | PAIP2019                                             | 418324   |
|           | PAIP2020-384                                         | PAIP2020                                             | 292889   |
|           | PAIP2021-384                                         | PAIP2021                                             | 1281320  |
|           | Post-NAT-BRCA-384                                    | Post-NAT-BRCA                                        | 116113   |
|           | TCGA-ACC-384                                         | TCGA-ACC                                             | 1411425  |
|           | TCGA-BLCA-384                                        | TCGA-BLCA                                            | 2538723  |
|           | TCGA-BRCA-384                                        | TCGA-BRCA                                            | 4250479  |
|           | TCGA-CESC-384                                        | TCGA-CESC                                            | 974224   |
|           | TCGA-CHOL-384                                        | TCGA-CHOL                                            | 320853   |
|           | TCGA-COAD-384                                        | TCGA-COAD                                            | 1678645  |
|           | TCGA-DLBC-384                                        | TCGA-DLBC                                            | 178480   |
|           | TCGA-ESCA-384                                        | TCGA-ESCA                                            | 692734   |
|           | TCGA-GBM-384                                         | TCGA-GBM                                             | 3110549  |
|           | TCGA-HNSC-384                                        | TCGA-HNSC                                            | 1773537  |
|           | TCGA-KICH-384                                        | TCGA-KICH                                            | 859967   |
|           | TCGA-KIRC-384                                        | TCGA-KIRC                                            | 3951997  |
|           | TCGA-KIRP-384                                        | TCGA-KIRP                                            | 1529229  |
|           | TCGA-LGG-384                                         | TCGA-LGG                                             | 2951024  |
|           | TCGA-LIHC-384                                        | TCGA-LIHC                                            | 2087889  |
|           | TCGA-LUAD-384                                        | TCGA-LUAD                                            | 2727122  |
|           | TCGA-LUSC-384                                        | TCGA-LUSC                                            | 2768358  |
|           | TCGA-MESO-384                                        | TCGA-MESO                                            | 289152   |
|           | TCGA-OV-384                                          | TCGA-OV                                              | 2024439  |
|           | TCGA-PAAD-384                                        | TCGA-PAAD                                            | 932041   |
|           | TCGA-PCPG-384                                        | TCGA-PCPG                                            | 1101645  |
|           | TCGA-PRAD-384                                        | TCGA-PRAD                                            | 2316782  |
|           | TCGA-READ-384                                        | TCGA-READ                                            | 529220   |
|           | TCGA-SARC-384                                        | TCGA-SARC                                            | 2904458  |
|           | TCGA-SKCM-384                                        | TCGA-SKCM                                            | 2111225  |
|           | TCGA-STAD-384                                        | TCGA-STAD                                            | 2484690  |
|           | TCGA-TGCT-384                                        | TCGA-TGCT                                            | 1129444  |
|           | TCGA-THCA-384                                        | TCGA-THCA                                            | 2732362  |
|           | TCGA-THYM-384                                        | TCGA-THYM                                            | 830621   |
|           | TCGA-UCEC-384                                        | TCGA-UCEC                                            | 3669664  |
|           | TCGA-UCS-384                                         | TCGA-UCS                                             | 461682   |
|           | TCGA-UVM-384                                         | TCGA-UVM                                             | 178380   |
| ROIs      | BreaKHis_100x                                        | BreakHis                                             | 2081     |
|           | BreaKHis_200x                                        | BreakHis                                             | 2013     |
|           | BreaKHis_400x                                        | BreakHis                                             | 1820     |
|           | BreastCancerCells                                    | Breast Cancer Cell Segmentation                      | 58       |
|           | BreastPathQ                                          | SPIE-AAPM-NCI BreastPathQ                            | 3696     |
|           | BreCaHAD                                             | BreCaHAD                                             | 162      |
|           | Chaoyang                                             | Chaoyang                                             | 6160     |
|           | Colorectal Histology MNIST                           | Colorectal Histology MNIST                           | 5002     |
|           | CoNSeP                                               | CoNSeP                                               | 41       |
|           | CRChistophenotypes                                   | CRCHistoPhenotypes - Labeled Cell Nuclei Data        | 100      |
|           | CRC-TP                                               | CRC-TP                                               | 30616    |
|           | CRC-VAL-HE-7K                                        | CRC-VAL-HE-7K                                        | 7180     |
|           | CryoNuSeg                                            | CryoNuSeg                                            | 30       |
|           | DataBiox_20x_40x                                     | DataBiox                                             | 193      |
|           | GasHisSDB_160                                        | GasHisSDB                                            | 32052    |
|           | Gastrointestinal_Cancer                              | Gastrointestinal Cancer                              | 192312   |
|           | HuBMAP+HBA_512                                       | HuBMAP+HBA Tiled dataset 512x512                     | 12581    |
|           | Kumar(MoNuSeg)                                       | MoNuSeg                                              | 51       |
|           | LizardDataset                                        | Lizard Dataset                                       | 238      |
|           | Lung_and_Colon_Cancer_Histopathological_Images_Colon | Lung and Colon Cancer Histopathological Images_Colon | 10000    |
|           | Lung_and_Colon_Cancer_Histopathological_Images_Lung  | Lung and Colon Cancer Histopathological Images_Lung  | 15000    |
|           | MoNuSAC                                              | MoNuSAC                                              | 294      |
|           | Monuseg_train&test                                   | PNG-converted-original-monuseg                       | 32       |
|           | Naylor et al, IEEE TMI 2019                          | Naylor et. al., IEEE TMI 2019                        | 50       |
|           | NCT-CRC-HE-100K                                      | NCT-CRC-HE-100K                                      | 100000   |
|           | PCam                                                 | Patch Camelyon                                       | 220025   |
|           | SICAPv2                                              | SICAPv2                                              | 18783    |
|           | Weinart et al, Scientific Reports 2012               | Weinart et. al., Scientific Reports 2012             | 36       |
|           | WSSS4LUAD                                            | WSSS4LUAD                                            | 10171    |
| Total     |                                                      |                                                      | 69515046 |
### S Scale
| Data type | Sub-dataset name     | Original name                           | Number   |
|-----------|----------------------|-----------------------------------------|----------|
| WSIs      | CAM16-96             | Camelyon16                              | 247449   |
|           | CATCH dataset-96     | CATCH                                   | 1350367  |
|           | CMB-CRC-96           | CMB-CRC                                 | 22493    |
|           | CMB-LCA-96           | CMB-LCA                                 | 3385     |
|           | CMB-MEL-96           | CMB-MEL                                 | 59324    |
|           | CPTAC-AML-96         | CPTAC-AML                               | 89199    |
|           | CPTAC-BRCA-96        | CPTAC-BRCA                              | 617563   |
|           | CPTAC-CCRCC-96       | CPTAC-CCRCC                             | 608736   |
|           | CPTAC-CM-96          | CPTAC-CM                                | 223379   |
|           | CPTAC-COAD-96        | CPTAC-COAD                              | 420512   |
|           | CPTAC-HNSCC-96       | CPTAC-HNSCC                             | 495941   |
|           | CPTAC-LSCC-96        | CPTAC-LSCC                              | 528998   |
|           | CPTAC-LUAD-96        | CPTAC-LUAD                              | 2452885  |
|           | CPTAC-OV-96          | CPTAC-OV                                | 190508   |
|           | CPTAC-PDA-96         | CPTAC-PDA                               | 371669   |
|           | CPTAC-SAR-96         | CPTAC-SAR                               | 352930   |
|           | CPTAC-UCEC-96        | CPTAC-UCEC                              | 733658   |
|           | HER2 tumor ROIs-96   | HER2 tumor ROIs                         | 75626    |
|           | MSKCC(SLN-Breast)-96 | MSKCC(SLN-Breast)                       | 126583   |
|           | PAIP2019-96          | PAIP2019                                | 414250   |
|           | PAIP2020-96          | PAIP2020                                | 285506   |
|           | PAIP2021-96          | PAIP2021                                | 1241781  |
|           | Post-NAT-BRCA-96     | Post-NAT-BRCA                           | 112502   |
|           | TCGA-ACC-96          | TCGA-ACC                                | 1385697  |
|           | TCGA-BLCA-96         | TCGA-BLCA                               | 2460390  |
|           | TCGA-BRCA-96         | TCGA-BRCA                               | 4118589  |
|           | TCGA-CESC-96         | TCGA-CESC                               | 949476   |
|           | TCGA-CHOL-96         | TCGA-CHOL                               | 316692   |
|           | TCGA-COAD-96         | TCGA-COAD                               | 1621830  |
|           | TCGA-DLBC-96         | TCGA-DLBC                               | 175767   |
|           | TCGA-ESCA-96         | TCGA-ESCA                               | 676850   |
|           | TCGA-GBM-96          | TCGA-GBM                                | 3025748  |
|           | TCGA-HNSC-96         | TCGA-HNSC                               | 1734134  |
|           | TCGA-KICH-96         | TCGA-KICH                               | 836947   |
|           | TCGA-KIRC-96         | TCGA-KIRC                               | 3839958  |
|           | TCGA-KIRP-96         | TCGA-KIRP                               | 1489190  |
|           | TCGA-LGG-96          | TCGA-LGG                                | 2875463  |
|           | TCGA-LIHC-96         | TCGA-LIHC                               | 2051973  |
|           | TCGA-LUAD-96         | TCGA-LUAD                               | 2617563  |
|           | TCGA-LUSC-96         | TCGA-LUSC                               | 2677495  |
|           | TCGA-MESO-96         | TCGA-MESO                               | 281741   |
|           | TCGA-OV-96           | TCGA-OV                                 | 1939530  |
|           | TCGA-PAAD-96         | TCGA-PAAD                               | 907570   |
|           | TCGA-PCPG-96         | TCGA-PCPG                               | 1074796  |
|           | TCGA-PRAD-96         | TCGA-PRAD                               | 2239750  |
|           | TCGA-READ-96         | TCGA-READ                               | 512094   |
|           | TCGA-SARC-96         | TCGA-SARC                               | 2855127  |
|           | TCGA-SKCM-96         | TCGA-SKCM                               | 2067692  |
|           | TCGA-STAD-96         | TCGA-STAD                               | 2422151  |
|           | TCGA-TGCT-96         | TCGA-TGCT                               | 1119804  |
|           | TCGA-THCA-96         | TCGA-THCA                               | 2640995  |
|           | TCGA-THYM-96         | TCGA-THYM                               | 814893   |
|           | TCGA-UCEC-96         | TCGA-UCEC                               | 3596205  |
|           | TCGA-UCS-96          | TCGA-UCS                                | 453748   |
|           | TCGA-UVM-96          | TCGA-UVM                                | 172984   |
| ROIs      | AML_Cytomorphology   | AML-Cytomorphology_LMU                  | 18365    |
|           | BCCD                 | BCCD                                    | 361      |
|           | Blood_Cell_Images    | Blood Cell Images                       | 9957     |
|           | GasHisSDB_80         | GasHisSDB                               | 146651   |
|           | LISC                 | LISC                                    | 250      |
|           | P_falciparum         | P. falciparum(ThickBloodSmears_150)     | 1883     |
|           | P_uninfected         | P.uninfected(NIH-NLM-ThickBloodSmearsU) | 1141     |
|           | P_vivax              | P. vivax（NIH-NLM-ThickBloodSmearsPV)    | 3014     |
|           | SIPaKMeD             | SIPaKMeD                                | 1004     |
|           | WBC                  | Raaim-WBC                               | 16633    |
| Total     |                      |                                         | 67177345 |

## Download

Due to the large-scale of CPIA, we divided the CPIA dataset into nine parts and put them in the SicenceDB data platform. Users can find the specific location of each sub-database in the CPIA_summary.excel under the dataset folder. Here are all the data links:

Part01: https://www.scidb.cn/detail?dataSetId=e481637377534fa7994cb582bcec440a

Part02: https://www.scidb.cn/detail?dataSetId=1d693905f1194e558a54bd3d1c9f6047

Part03: https://www.scidb.cn/detail?dataSetId=bea2da91bbc24ca3838150acc0565609

Part04: https://www.scidb.cn/detail?dataSetId=8e003efabab74c1699b3fd297b5e7da9

Part05: https://www.scidb.cn/detail?dataSetId=7be592a6a89149249f10f9f8d8ed73d4

Part06: https://www.scidb.cn/detail?dataSetId=f3a0f811b5e248cdab6b397d69daaf91

Part07: https://www.scidb.cn/detail?dataSetId=1246be5dbb6b41959205851739a5d6b3

Part08: https://www.scidb.cn/detail?dataSetId=bf97c631e5034cde848466408ec42ae0

Part09: https://www.scidb.cn/detail?dataSetId=5a1b4bef78954f4d9d31832efa38189c

