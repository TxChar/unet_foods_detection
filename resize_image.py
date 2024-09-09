import os
from PIL import Image

# ตั้งค่าขนาดใหม่ที่ต้องการรีไซส์
new_size = (640, 640)

# กำหนดโฟลเดอร์สำหรับอ่านและบันทึกรูปภาพ
input_folder = 'data/dataset/SegmentationClass/'
output_folder = 'data/images_resize/'

# สร้างโฟลเดอร์สำหรับบันทึกรูปภาพรีไซส์แล้ว ถ้าโฟลเดอร์ยังไม่มี
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# วนลูปอ่านไฟล์รูปภาพในโฟลเดอร์
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # ตรวจสอบว่าเป็นไฟล์รูปภาพ
        # เปิดรูปภาพ
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # รีไซส์รูปภาพ
        resized_img = img.resize(new_size)

        # บันทึกรูปภาพที่รีไซส์แล้ว
        output_path = os.path.join(output_folder, filename)
        resized_img.save(output_path)

        print(f"Resized {filename} and saved to {output_folder}")

print("Resize complete!")
