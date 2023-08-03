from PIL import Image
import os

# 取得資料夾A,B 中的所有檔案名稱
a_files = os.listdir(r".\A")
b_files = os.listdir(r".\B")
print(a_files)
print(b_files)

times = 0

# 遍歷資料夾A中的每個檔案
for a_file in a_files:
    print(a_file)

    img_a = Image.open(os.path.join(r".\A", a_file))
    img_b = Image.open(os.path.join(r".\B", b_files[times]))

    # 取得資料夾B中圖片的寬度和高度
    width_b, height_b = img_b.size

    # 建立一個新的透明圖像，大小為資料夾B中圖片的尺寸，背景顏色為完全透明
    # 將資料夾A中的圖片貼到新圖像上，位置為居中對齊
    new_image = Image.new('RGBA', (width_b, height_b), color=(0,0,0,0))
    new_image.paste(img_a, ((width_b - img_a.width) // 2, (height_b - img_a.height) // 2))
    
    # 取得檔名（去除副檔名部分）
    # 儲存新圖像到fixed資料夾下，檔名為原始檔案名稱加上.png的副檔名
    file_name = os.path.splitext(a_file)[0]
    new_image.save(f"./fixed/{file_name}.png")
    
    times = times + 1
    print("修改第" + str(times) + "張")
