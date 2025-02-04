import csv
import random
from enum import Enum
from dataclasses import dataclass

class Attribute:
   pass

@dataclass
class Student:
   timestamp: str
   student_id: str
   name: str
   department: str
   grade: str
   double_major_minor_second_speciality: str
   first_choice: str
   second_choice: str
   weight: float = 0.0
   result: str = ""
   
def calculateWeight(student: Student) -> float:
   weight = random.random()
         
   if student.department == '資工系 (CS)' or student.department == '電資學院學士班 (U-EECS)':            
      if student.grade == '大二 (sophomore)':               
      # 第一優先: 資工系大二
         return 10 + weight
      elif student.grade == '大三 (junior)':
      # 第三優先: 資工系大三
         return 30 + weight
      else:
      # 第二優先: 資工系大四 or 更高年級
         return 20 + weight
   elif student.double_major_minor_second_speciality == '雙主修:資工系 (also major in CS)':
      # 第三優先: 雙主修資工者
      return 30 + weight
   else:
      # 第四優先: 其他
      return 40 + weight

def allocateStudent(students, limitLee = 40, limitKao = 40, adjustment = 3):
   distribution_results = {
        "李教授班": [],
        "高教授班": [],
        "志願序不符合規定": [],
        "調整名單":[]
   }
   
   countLee, countKao, countAdjust = 0, 0, 0

   for student in students:
      if student.first_choice == "無":
         allocation = "志願序不符合規定" 
                 
      elif student.first_choice == "李教授班" and countLee < limitLee:
         allocation = "李教授班"
         countLee = countLee + 1
                  
      elif student.first_choice == "高教授班" and countKao < limitKao:
         allocation = "高教授班"
         countKao = countKao + 1
         
      elif student.second_choice == "無":
         continue
               
      elif student.second_choice == "李教授班" and countLee < limitLee:
         allocation = "李教授班"
         countLee = countLee + 1
                  
      elif student.second_choice == "高教授班" and countKao < limitKao:
         allocation = "高教授班"
         countKao = countKao + 1          
      # 小問題，如果第一志願沒上，第二志願填無，會跑來調整名單 
      # 好像沒問題? 在調整名單的都是 志願 1,2 都有填，但名額滿了      
      elif countAdjust < adjustment:
         allocation = "調整名單"
         countAdjust += 1
      else:
         break

      student.result = allocation            
      distribution_results[allocation].append(student)      

   return distribution_results

if __name__ == '__main__':
   with open('data_v1.csv', mode='r', encoding='utf-8') as file:
      csv_reader = csv.reader(file)
      
      header = next(csv_reader)  # 取得欄位標題      
      students = [
         Student(
            timestamp = data[0],
            student_id = data[1], 
            name = data[2], 
            department = data[3], 
            grade = data[4], 
            double_major_minor_second_speciality = data[5], 
            first_choice = data[6], 
            second_choice = data[7],
            weight = calculateWeight(Student(*data)) 
         )                  
         for data in csv_reader
      ]
      
      students.sort(key = lambda s: s.weight)
      distributionResults = allocateStudent(students)  
      
      print("分發結果：")
      for key, value in distributionResults.items():
         print(f"{key} 分發的學生:")
         
         for student in value:
            if student.result == "調整名單":
               print(f"{student.weight}, {student.student_id}, {student.name}, {student.department}, {student.grade}, {student.first_choice}, {student.second_choice}")
            elif student.result == "志願序不符合規定":
               print(f"{student.weight}, {student.student_id}, {student.name}, {student.department}, {student.grade}")               
            else:
               print(f"{student.weight}, {student.student_id}, {student.name}, {student.department}, {student.grade}, {student.result}")
         print("\n")
      
              
      #存檔    
      with open('resultFunc.csv', mode='w', encoding='utf-8', newline='') as output_file:
         csv_writer = csv.writer(output_file)
         csv_writer.writerow(["student_id", "name", "department", "grade", "double_major", "first_choice", "second_choice", "weight", "result"])
         csv_writer.writerows([[s.student_id, s.name, s.department, s.grade, s.double_major_minor_second_speciality, 
                                s.first_choice, s.second_choice, s.weight, s.result] for s in students])
