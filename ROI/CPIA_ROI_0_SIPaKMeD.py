"""
CPIA_ROI_0_SIPaKMeD.py
This code aims to split test/train pictures and img/annotation pictures into different folders
The original SIPaKMeD dataset has a CROPPED part inside the folder of each class. This code splits
the original view images and cropped images into two folders.
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
    # del_file(file_pack_path)


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
    return res


def save_file(f_image, save_dir, suffix='.jpg'):
    filepath, _ = os.path.split(save_dir)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    f_image.save(save_dir + suffix)


def pc_to_stander(root_from, root_to):
    root_target = root_to
    make_and_clear_path(root_target)

    f_dir_list = find_all_files(root=root_from, suffix=".bmp")
    print(f_dir_list)
    name_dict = {}
    i1 = 0
    i2 = 0
    i3 = 0
    i4 = 0
    i5 = 0

    for seq in tqdm(range(len(f_dir_list))):
        f_dir = f_dir_list[seq]

        f_img = Image.open(f_dir)


        if 'im_Superficial-Intermediate' in f_dir:
            if 'CROPPED' in f_dir:
                root_target = os.path.join(root_to, 'Cropped')
            else:
                root_target = os.path.join(root_to, "Full")
            root_target = os.path.join(root_target, 'Sup_Intermediate')
            i1 += 1
            save_dir = os.path.join(root_target, str(i1))
        elif 'im_Parabasal' in f_dir:
            if 'CROPPED' in f_dir:
                root_target = os.path.join(root_to, 'Cropped')
            else:
                root_target = os.path.join(root_to, "Full")
            root_target = os.path.join(root_target, 'Parabasal')
            i2 += 1
            save_dir = os.path.join(root_target, str(i2))
        elif 'im_Dyskeratotic' in f_dir:
            if 'CROPPED' in f_dir:
                root_target = os.path.join(root_to, 'Cropped')
            else:
                root_target = os.path.join(root_to, "Full")
            root_target = os.path.join(root_target, 'Dyskeratotic')
            i3 += 1
            save_dir = os.path.join(root_target, str(i3))
        elif 'im_Koilocytotic' in f_dir:
            if 'CROPPED' in f_dir:
                root_target = os.path.join(root_to, 'Cropped')
            else:
                root_target = os.path.join(root_to, "Full")
            root_target = os.path.join(root_target, 'Koilocytotic')
            i4 += 1
            save_dir = os.path.join(root_target, str(i4))
        else:
            if 'CROPPED' in f_dir:
                root_target = os.path.join(root_to, 'Cropped')
            else:
                root_target = os.path.join(root_to, "Full")
            root_target = os.path.join(root_target, 'Metaplastic')
            i5 += 1
            save_dir = os.path.join(root_target, str(i5))

        name_dict[save_dir] = f_dir

        save_file(f_img, save_dir)


if __name__ == '__main__':
    args = get_args_parser()
    args = args.parse_args()

    input_root = args.input_root
    output_root = args.output_root

    pc_to_stander(input_root, output_root)