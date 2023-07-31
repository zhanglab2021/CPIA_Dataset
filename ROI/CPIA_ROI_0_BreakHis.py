"""
CPIA_ROI_0_BreakHis.py  ver 23.6.9
This code aims to split images of different zooming size into different folders,this code also puts different classes
into different folders
"""
import argparse
import os
from PIL import Image
from tqdm import tqdm


def get_args_parser():
    parser = argparse.ArgumentParser('CPIA dataset ROI part Warwick_QU dataset pre-processing', add_help=False)
    parser.add_argument('--input_root', default='..', type=str,
                        help='The root that contains the orginal images. Please make sure that there is no unwanted '
                             'images with corresponding suffix under the same root')
    parser.add_argument('--output_root', default='..', type=str,
                        help='The root for the resized and cropped output images. If the root is not provided, this '
                             'program will automatically make an output path')
    return parser


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
    print(res)
    print(len(res))
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
        _, str = os.path.split(f_dir)
        mp = str.split("-")[-2]
        type = (str.split("_")[2]).split("-")[0]
        name = str.split(".")[0]
        print(mp)
        print(type)

        f_img = Image.open(f_dir)
        if mp == '40':
            root_target = os.path.join(root_to, '40')
        elif mp == '100':
            root_target = os.path.join(root_to, '100')
        elif mp == '200':
            root_target = os.path.join(root_to, '200')
        else:
            root_target = os.path.join(root_to, '400')
        if type == 'DC':
            root_target = os.path.join(root_target, 'ductal_carcinoma')
        elif type == 'LC':
            root_target = os.path.join(root_target, 'lobular_carcinoma')
        elif type == 'MC':
            root_target = os.path.join(root_target, 'mucinous_carcinoma')
        elif type == 'PC':
            root_target = os.path.join(root_target, 'papillary_carcinoma')
        elif type == 'A':
            root_target = os.path.join(root_target, 'adenosis')
        elif type == 'F':
            root_target = os.path.join(root_target, 'fibroadenoma')
        elif type == 'PT':
            root_target = os.path.join(root_target, 'phyllodes_tumor')
        else:
            root_target = os.path.join(root_target, 'tubular_adenoma')

        save_dir = os.path.join(root_target, name)


        name_dict[save_dir] = f_dir

        save_file(f_img, save_dir)

    root_target, _ = os.path.split(root_to)
    root_target, _ = os.path.split(root_target)

if __name__ == '__main__':
    args = get_args_parser()
    args = args.parse_args()

    input_root = args.input_root
    output_root = args.output_root

    pc_to_stander(input_root, output_root)










