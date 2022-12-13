# -*- coding: EUC-KR -*-
from openpyxl import load_workbook

import keyboard
import random
import time
import hgtk
import os

load_wb = load_workbook("text.xlsx", data_only=True)
TEXT = load_wb['Sheet1']

text_list = []

get_cells = TEXT['A1' : 'A728']

for row in get_cells:
    for cell in row:
        text_list.append(cell.value)

get_cells = TEXT['A762' : 'A35052']
for row in get_cells:
    for cell in row:
        text_list.append(cell.value)

get_cells = TEXT['B1' : 'B35052']
for row in get_cells:
    for cell in row:
        text_list.append(cell.value)
        
random.shuffle(text_list)
list_len = len(text_list)
current_count = 0;
game_size = int(input("몇문제를 풀것입니까?\n"))
typing_speed = []
accuracy = []
#os.system("pause")
#while current_count < list_len:
#while True:
while current_count < game_size:
    os.system("cls")

    q = text_list[current_count]
    current_count +=1

    start_time = time.time()
    user_input = input(q + '\n')
    end_time = time.time() - start_time


    src = hgtk.text.decompose(q).replace("?","")
    tar = hgtk.text.decompose(user_input).replace("?","")
    
    correct = 0
    for i, c in enumerate(src, start = 0):
        try:
            if tar[i] == c :
                correct += 1
        except:
            pass
    
    src_len = len(src)
    c  = correct / src_len *100 # 
    e = (src_len - correct) / src_len * 100 # 

    speed = float(correct / end_time) *60
    print("\n타자 속도 : {:0.1f}타, 정확도 : {:0.2f}%, 오타율 : {:0.2f}%\n".format(speed,c,e))
    typing_speed.append(speed)
    accuracy.append(c)
    os.system("pause")

print("\n\t최고 속도 : {:0.1f}타\t 최고 정확도 : {:0.1f}%".format(max(typing_speed), max(accuracy) ))
print("\t평균 속도 : {:0.1f}타\t 평균 정확도 : {:0.2f}%".format(sum(typing_speed)/len(typing_speed), sum(accuracy)/len(accuracy)))
print("\t최저 속도 : {:0.1f}타\t 최저 정확도 : {:0.1f}%\n".format(min(typing_speed),min(accuracy)))
print("아무 키나 누르면 게임을 종료합니다.")
os.system("pause")