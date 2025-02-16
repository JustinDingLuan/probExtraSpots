import csv
import random
from enum import Enum

class Attribute:
   pass

if __name__ == '__main__':
   with open('data_v1.csv', mode='r', encoding='utf-8') as file:
      csv_reader = csv.reader(file)
      
      header = next(csv_reader)  # 取得欄位標題
      header.append('weight')
      header.append('result')
      print("欄位標題:", header)
      
      attribute = Enum('Attribute', {name: idx for idx, name in enumerate(header)})      
      
      records = [row for row in csv_reader]
      
      for data in records:
         weight = random.random()
         
         if data[attribute.department.value] == '資工系 (CS)' or data[attribute.department.value] == '電資學院學士班 (U-EECS)':            
            if data[attribute.grade.value] == '大二 (sophomore)':               
            # 第一優先: 資工系大二
               data.append(10 + weight)               
            elif data[attribute.grade.value] == '大三 (junior)':
            # 第三優先: 資工系大三
               data.append(30 + weight)               
            else:
            # 第二優先: 資工系大四 or 更高年級
               data.append(20 + weight)         
         elif data[attribute.double_major_minor_second_speciality.value] == '雙主修:資工系 (also major in CS)':
            # 第三優先: 雙主修資工者
            data.append(30 + weight)
         else:
            # 第四優先: 其他
            data.append(40 + weight)
               
      records.sort(key = lambda row: row[attribute.weight.value])   
      
      distributionResults = {
         '李教授班': [],
         '高教授班': [],
         '志願序不符合規定': [],
         '未分發':[]
         # '調整名單':[]                     
      }
      
      # 設定每班限制加簽人數
      limitLee = 40
      limitKao = 40
      countLee = 0
      countKao = 0
      
      #彈性調整
      # Adjustment = 3
      # countAdjust = 0
      
      # 進行分發
      # 規則: 
      # 1.第一志願不可填無，如果填了代表不想加簽? 
      # 2.第二志願若填無，表示不想去另一班
      
      for data in records:
         allocation = ''         
         if data[attribute.first_choice.value] == '無':
            allocation = '志願序不符合規定'
            
         elif data[attribute.first_choice.value] == '李教授班' and countLee < limitLee:
            countLee += 1
            allocation = '李教授班'
            
         elif data[attribute.first_choice.value] == '高教授班' and countKao < limitKao:
            countKao += 1
            allocation = '高教授班'
            
         # elif data[attribute.second_choice.value] == '無':
         #    continue
         
         elif data[attribute.second_choice.value] == '李教授班' and countLee < limitLee:
            countLee += 1
            allocation = '李教授班'
            
         elif data[attribute.second_choice.value] == '高教授班' and countKao < limitKao:
            countKao += 1
            allocation = '高教授班'
         # 彈性調整  這邊還要再確認一下? 
         # elif countAdjust < Adjustment:
         #    allocation = '調整名單'            
         #    countAdjust += 1
         else:  
            allocation = '未分發'
            # break
         
         data.append(allocation)
         # data.append(f"分發結果: {allocation}")
         
         
         # selectedData = [
         #    data[attribute.weight.value],
         #    data[attribute.student_id.value],
         #    data[attribute.name.value],
         #    data[attribute.department.value],
         #    data[attribute.grade.value]
         # ]
         # # if allocation == '調整名單':
         # #    selectedData.append([data[attribute.first_choice.value], data[attribute.second_choice.value]])
            
         # distributionResults[allocation].append(selectedData)
      
      # 讓資料根據分發結果排序，並且同組內根據 weight 進行排序
      # records.sort(key=lambda row: (row[attribute.result.value], -row[attribute.weight.value]), reverse = True)

      # print("分發結果：")
      # for key, value in distributionResults.items():
      #    print(f"{key} 分發的學生：")
         
      #    for student in value:
      #       print(student)
      #    print('\n')
      # print(attribute.weight.value) 
             
      #存檔    
      with open('result.csv', mode='w', encoding='utf-8', newline='') as output_file:
         csv_writer = csv.writer(output_file)
         csv_writer.writerow(header)         
         csv_writer.writerows(records) 