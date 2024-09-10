import os
from PIL import Image

# ตั้งค่าขนาดใหม่ที่ต้องการรีไซส์
new_size = (224, 224)

# กำหนดโฟลเดอร์สำหรับอ่านและบันทึกรูปภาพ
input_folder = "data/images/"
output_folder = "resize_images/sources/"

# สร้างโฟลเดอร์สำหรับบันทึกรูปภาพรีไซส์แล้ว ถ้าโฟลเดอร์ยังไม่มี
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# วนลูปอ่านไฟล์รูปภาพในโฟลเดอร์
for filename in os.listdir(input_folder):
    if filename.endswith(
        (".png", ".jpg", ".jpeg", ".bmp", ".gif")
    ):  # ตรวจสอบว่าเป็นไฟล์รูปภาพ
        # เปิดรูปภาพ
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # รีไซส์รูปภาพ
        resized_img = img.resize(new_size)

        # ตรวจสอบว่ารูปภาพเป็น RGB หรือไม่ ถ้าไม่ใช่ให้แปลงเป็น RGB
        if resized_img.mode != "RGB":
            resized_img = resized_img.convert("RGB")

        # เปลี่ยนชื่อไฟล์ให้เป็น .jpg
        output_filename = os.path.splitext(filename)[0] + ".jpg"
        output_path = os.path.join(output_folder, output_filename)

        # บันทึกรูปภาพที่รีไซส์แล้วเป็น .jpg
        resized_img.save(output_path, "JPEG")

        print(f"Resized {filename} and saved as {output_filename} to {output_folder}")

print("Resize complete!")
