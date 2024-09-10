import os
from PIL import Image, ImageFilter
import imgaug.augmenters as iaa
import numpy as np

input_folder = "data/images"
output_folder = "augmentation_data/images"

# input_folder = "data/dataset/SegmentationClassResize"
# output_folder = "augmentation_data/SegmentationClassResize"

# สร้างโฟลเดอร์ output หากยังไม่มี
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ออปเจกต์สำหรับการ augment
augmenters = {
    "0": "None",
    "1": iaa.Fliplr(1.0),
    "2": iaa.Affine(rotate=90),
    "3": iaa.AverageBlur(6),
    "4": iaa.Crop(percent=(0, 0.2)),
}


# ฟังก์ชันในการบันทึกภาพ
def save_image(image, file_name, augment_type):
    file_path = os.path.join(output_folder, f"{file_name}_{augment_type}.jpg")
    image.save(file_path)


# อ่านและปรับภาพ
for file_name in os.listdir(input_folder):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        img_path = os.path.join(input_folder, file_name)
        image = Image.open(img_path)

        for augment_name, augmenter in augmenters.items():
            # การทำงานของ imgaug ต้องใช้ numpy array
            image_np = np.array(image)

            if augment_name == "0":
                save_image(image, file_name.split(".")[0], augment_name)
            elif augment_name == "3" and "SegmentationClassResize" in input_folder:
                save_image(image, file_name.split(".")[0], augment_name)
            else:
                # ทำการ augment
                augmented_image_np = augmenter(image=image_np)
                # เปลี่ยนกลับเป็นภาพ PIL
                augmented_image = Image.fromarray(augmented_image_np)
                save_image(augmented_image, file_name.split(".")[0], augment_name)

        print(f"Processed {file_name}")
print("Processing complete.")
