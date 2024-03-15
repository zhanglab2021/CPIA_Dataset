import os
import PIL.Image as Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None


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


def center_crop(img_size):
    """
    Return the cropping zone of a non-square image
    :param img_size: img.size
    :return: list that contains the cropping zone
    """
    width, height = img_size  # Get dimensions
    a = min(width, height)
    left = int((width - a) / 2)
    top = int((height - a) / 2)
    right = left + a
    bottom = top + a

    return [left, top, right, bottom]


def data_crop_resize(class_root, output_root, suffix, size=384):
    all_data = find_all_files(class_root, suffix)
    for data_root in all_data:
        if data_root.endswith('.txt'):
            continue
        elif data_root.endswith('.DS_Store'):
            continue
        elif output_root is None:
            new_data_root = (data_root + '_Lite').split('.')[0]
            # specially made for GS dataset:
            """new_data_root = (data_root + '_Lite').replace('.', '_')
            new_data_root = new_data_root.replace('_jpg', '')"""
        else:
            data_name_without_suffix = os.path.split(data_root)[1].split('.')[0]
            new_data_root = os.path.join(output_root, data_name_without_suffix)


        img = Image.open(data_root)
        width, height = img.size  # Get dimensions
        s = min(width, height)
        """left = int((width - a) / 2)
        top = int((height - a) / 2)
        right = left + a
        bottom = top + a
        this is DataBiox
        """

        """a = int((s * 5) / 7)
        da = int(s / 14)
        top = int(s / 7) + da
        bottom = top + a - 2 * da

        left = int(s / 7) + 4*da
        right = left + a - 2 * da
        this is for P.vivax"""

        """a = int((s * 5) / 7)
        da = int(s / 14)
        top = int(s / 7) + 3* da
        bottom = top + a - 4 * da

        left = int(s / 7) + 4 * da
        right = left + a - 2 * da
        this is for P_falciparum"""

        a = int((s * 5) / 7)
        da = int(s / 14)
        top = int(s / 7) + 2 * da
        bottom = top + a - 2 * da

        left = int(s / 7) + 4 * da
        right = left + a - 4 * da


        # Crop the center of the image
        img = img.crop([left, top, right, bottom])
        resized_img = img.resize((int(size), int(size)), Image.ANTIALIAS)
        save_file(resized_img, new_data_root)


if __name__ == '__main__':
    data_crop_resize(r'F:\Puzzle Tuning Datasets\P.uninfected(NIH-NLM-ThickBloodSmearsU)\NIH-NLM-ThickBloodSmearsU\Uninfected Patients',
                     r'D:\CPIA_VersionJournal\CPIA_MJ\S\P_uninfected',
                     'tiff',
                     384)