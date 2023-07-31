"""
CPIA_ROI_0_GasHisSDB.py  ver 23.6.9
This code aims to split images of different zooming size into different folders, this code also puts different classes
into different folders
"""

import argparse
import os
import re
import csv
import shutil
import pandas as pd
from PIL import Image
from tqdm import tqdm
import torchvision.transforms


def get_args_parser():
    parser = argparse.ArgumentParser('CPIA dataset ROI part Warwick_QU dataset pre-processing', add_help=False)
    parser.add_argument('--input_root', default='..', type=str,
                        help='The root that contains the orginal images. Please make sure that there is no unwanted '
                             'images with corresponding suffix under the same root')
    parser.add_argument('--output_root', default='..', type=str,
                        help='The root for the resized and cropped output images. If the root is not provided, this '
                             'program will automatically make an output path')
    return parser


def del_file(filepath):
    """
    Delete all files and folders in one directory
    :param filepath: file path
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def make_and_clear_path(file_pack_path):
    if not os.path.exists(file_pack_path):
        os.makedirs(file_pack_path)


def find_all_files(root, suffix=None):
    """
    Return a list of file paths ended with specific suffix
    """
    res = []
    for root, _, files in os.walk(root):
        for f in files:
            if suffix is not None and not f.endswith(suffix):
                continue
            res.append(os.path.join(root, f))
        print(files)
    return res


def save_file(f_image, save_dir, suffix='.jpg'):

    filepath, _ = os.path.split(save_dir)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    f_image.save(save_dir + suffix)


def pc_to_stander(root_from, root_to):
    root_target = root_to
    make_and_clear_path(root_target)

    f_dir_list = find_all_files(root=root_from, suffix=".png")
    print(f_dir_list)
    name_dict = {}

    for seq in tqdm(range(len(f_dir_list))):
        f_dir = f_dir_list[seq]
        f_img = Image.open(f_dir)
        _, img_name = os.path.split(f_dir)
        name = img_name.split('.')[0]

        if '80' in f_dir:
            root_target = os.path.join(root_to, '80')
        elif '120' in f_dir:
            root_target = os.path.join(root_to, '120')
        else:
            root_target = os.path.join(root_to, '160')

        if 'Normal' in f_dir:
            save_dir = os.path.join(root_target, 'Normal')
        else:
            save_dir = os.path.join(root_target, 'Abnormal')

            """if img_name == result[i][0]:
                root_target = os.path.join(root_to, result[i][1])
                if result[i][1] == 0:
                    i1 += 1
                    save_dir = os.path.join(root_target, str(i1))
                elif result[i][1] == 1:
                    i2 += 1
                    save_dir = os.path.join(root_target, str(i2))
                else:
                    i3 += 1
                    save_dir = os.path.join(root_target, str(i3))
                break
            else:
                continue"""
        save_dir = os.path.join(save_dir, name)

        name_dict[save_dir] = f_dir

        save_file(f_img, save_dir)

    root_target, _ = os.path.split(root_to)
    root_target, _ = os.path.split(root_target)
    pd.DataFrame.from_dict(name_dict, orient='index', columns=['origin path']).to_csv(
        os.path.join(root_target, 'name_dict_gashis.csv')
    )


if __name__ == '__main__':
    args = get_args_parser()
    args = args.parse_args()

    input_root = args.input_root
    output_root = args.output_root

    pc_to_stander(input_root, output_root)