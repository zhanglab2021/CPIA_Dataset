"""
CPIA_ROI_1_Microscope_P_vivax.py  ver 23.6.8
This code aims to crop each Microscope image by the largest center square, keeping the black surroundings out of the
final image.
Also, all the images will be resized into 384*384 (or other size you want).
"""
import argparse
import os
import PIL.Image as Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None


def get_args_parser():
    parser = argparse.ArgumentParser('CPIA dataset ROI part image cropping and resizing', add_help=False)
    parser.add_argument('--input_root', default='..', type=str,
                        help='The root that contains the orginal images. Please make sure that there is no unwanted '
                             'images with corresponding suffix under the same root')
    parser.add_argument('--output_root', default=None, type=str,
                        help='The root for the resized and cropped output images. If the root is not provided, this '
                             'program will automatically make an output path')
    parser.add_argument('--suffix', default='jpg', type=str,
                        help='The suffix of the input image')
    parser.add_argument('--size', default=384, type=int,
                        help='The size of the output image')
    return argparse


def save_file(f_image, save_dir, suffix='.jpg'):
    """
    Save images with designated suffix
    """
    f_image = f_image.convert('RGB')
    filepath, _ = os.path.split(save_dir)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    f_image.save(save_dir + suffix)


def make_path(file_pack_path):
    if not os.path.exists(file_pack_path):
        os.makedirs(file_pack_path)


def find_all_files(root, suffix):
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


def data_crop_resize(class_root, output_root, suffix, size=384):
    all_data = find_all_files(class_root, suffix)
    for data_root in all_data:
        if data_root.endswith('.txt'):
            continue
        elif data_root.endswith('.DS_Store'):
            continue
        elif output_root is None:
            new_data_root = (data_root + '_Lite').split('.')[0]
        else:
            data_name_without_suffix = os.path.split(data_root)[1].split('.')[0]
            new_data_root = os.path.join(output_root, data_name_without_suffix)

        img = Image.open(data_root)
        width, height = img.size  # Get size

        # the cropping parameters are tuned for P_vivax
        s = min(width, height)
        a = int((s * 5) / 7)
        da = int(s / 14)
        top = int(s / 7) + da
        bottom = top + a - 2 * da

        left = int(s / 7) + 4 * da
        right = left + a - 2 * da

        # Crop the center of the image
        img = img.crop([left, top, right, bottom])
        resized_img = img.resize((int(size), int(size)), Image.ANTIALIAS)
        save_file(resized_img, new_data_root)


if __name__ == '__main__':
    args = get_args_parser()
    args = args.parse_args()

    input_root = args.input_root
    output_root = args.output_root
    suffix = args.suffix
    size = args.size
    data_crop_resize(input_root, output_root, suffix, size)