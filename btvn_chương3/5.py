import numpy as np

height = [70, 72, 75, 68, 74, 69, 73, 77, 78, 80]  
weight = [180, 200, 220, 160, 190, 175, 210, 230, 240, 250]  

arr_height = np.array(height)
arr_weight = np.array(weight)
conversion_factor_height = 0.0254
arr_height_m = arr_height * conversion_factor_height
conversion_factor_weight = 0.453592
arr_weight_kg = arr_weight * conversion_factor_weight

arr_bmi = arr_weight_kg / (arr_height_m ** 2)

weight_at_index_50 = arr_weight_kg[50] if len(arr_weight_kg) > 50 else None

arr_height_m_100 = arr_height_m[100:111] if len(arr_height_m) > 100 else None

players_bmi_less_than_21 = arr_bmi[arr_bmi < 21]

average_height = np.mean(arr_height_m)
average_weight = np.mean(arr_weight_kg)

max_height = np.max(arr_height_m)
max_weight = np.max(arr_weight_kg)

min_height = np.min(arr_height_m)
min_weight = np.min(arr_weight_kg)

# Kết quả
print("Chiều cao trung bình (m):", average_height)
print("Cân nặng trung bình (kg):", average_weight)
print("Chiều cao lớn nhất (m):", max_height)
print("Cân nặng lớn nhất (kg):", max_weight)
print("Chiều cao nhỏ nhất (m):", min_height)
print("Cân nặng nhỏ nhất (kg):", min_weight)
print("Giá trị cân nặng ở index 50:", weight_at_index_50)
print("Các cầu thủ có BMI < 21:", players_bmi_less_than_21)


# Đọc chiều cao từ heights_1.txt
with open('heights_1.txt', 'r') as file:
    height = [float(line.strip()) for line in file]

# Đọc cân nặng từ weights_1.txt
with open('weights_1.txt', 'r') as file:
    weight = [float(line.strip()) for line in file]

# Kiểm tra dữ liệu đã đọc
print("Chiều cao:", height)
print("Cân nặng:", weight)

import os
print(os.getcwd())
