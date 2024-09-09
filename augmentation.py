import os
from PIL import Image, ImageFilter
import imgaug.augmenters as iaa

# # กำหนด path ของโฟลเดอร์ที่มีภาพ
# input_folder = 'data/images'
# output_folder = 'augmentation_data/images'

# กำหนด path ของโฟลเดอร์ที่มีภาพ
input_folder = 'data/dataset/SegmentationClassResize'
output_folder = 'augmentation_data/SegmentationClassResize'

# สร้างโฟลเดอร์ output หากยังไม่มี
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ออปเจกต์สำหรับการ augment
augmenters = {
    'Flip': iaa.Fliplr(1.0),
    'Resize': iaa.Resize(0.5),
    'Rotate': iaa.Affine(rotate=45),
    'Blur': iaa.AverageBlur(3),
    'Crop': iaa.Crop(percent=(0, 0.2))
}

# ฟังก์ชันในการบันทึกภาพ
def save_image(image, file_name, augment_type):
    file_path = os.path.join(output_folder, f"{file_name}_{augment_type}.jpg")
    image.save(file_path)

# อ่านและปรับภาพ
for file_name in os.listdir(input_folder):
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        img_path = os.path.join(input_folder, file_name)
        image = Image.open(img_path)

        for augment_name, augmenter in augmenters.items():
            # การทำงานของ imgaug ต้องใช้ numpy array
            import numpy as np
            image_np = np.array(image)

            # ทำการ augment
            augmented_image_np = augmenter(image=image_np)

            # เปลี่ยนกลับเป็นภาพ PIL
            augmented_image = Image.fromarray(augmented_image_np)

            # บันทึกภาพ
            save_image(augmented_image, file_name.split('.')[0], augment_name)
        
        print(f"Processed {file_name}")

print("Processing complete.")
