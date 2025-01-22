import pandas as pd
from itertools import product


if __name__ == '__main__':
    departments = [
        '資工系 (CS)',
        '電機系 (EE)',
        '電資學院學士班 (U-EECS)',
        '其他'
    ]

    grades = [
        '大一 (freshman)',
        '大二 (sophomore)',
        '大三 (junior)',
        '大四 (senior)',
        '大五、大六、或大七',
        '其他'
    ]

    double_major_minor_second_speciality = [
        '雙主修:資工系 (also major in CS)',
        '輔系:資工系 (minor in CS)',
        '以「資訊工程」為第二專長 (second specialty in Computer Science)',
        '無'
    ]

    first_choice = [
        '李教授班',
        '高教授班',
        '無'
    ]
    second_choice = first_choice

    departments_ls, grades_ls, \
    double_major_minor_second_speciality_ls, \
    first_choice_ls, second_choice_ls = zip(*product(
        departments, grades,
        double_major_minor_second_speciality,
        first_choice, second_choice
    ))

    timestamp = pd.Timestamp.now()
    df = pd.DataFrame(
        data={
            'timestamp': [timestamp + pd.Timedelta(seconds=i) for i in range(len(departments_ls))],
            'student_id': range(1, len(departments_ls) + 1),
            'name': [f'student_{i}' for i in range(1, len(departments_ls) + 1)],
            'department': departments_ls,
            'grade': grades_ls,
            'double_major_minor_second_speciality': double_major_minor_second_speciality_ls,
            'first_choice': first_choice_ls,
            'second_choice': second_choice_ls
        }
    )
    
    df_new = df.copy()
    df_new['timestamp'] = [timestamp + pd.Timedelta(hours=1, seconds=i) for i in range(len(departments_ls))]

    # 總共有 864 x 2 筆資料
    # 1. 故意讓資料重複
    # 2. 故意倒過來 concat 讓時間比較晚的在 dataframe 的前段
    df = pd.concat([df_new, df], ignore_index=True)
    
    df.to_csv('data.csv', index=False)

    ########### 去除重複資料可以用這個 ###########
    # idx = df.groupby(['student_id', 'name'])['timestamp'].idxmax()
    # df = df.loc[idx]
    # print(df)
    ###########
