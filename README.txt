程式流程: 
1. gen_data.py ->生成資料(data.csv)
2. remove_repeat_data.py ->移除重複資料(data_v1.csv)
3. signProcess_v1.py ->用data_v1.csv去跑出隨機亂數並分發(result.csv)
4. 用 excel 開的話，要用匯入 csv 檔的方式 => 資料 -> 從 csv -> 載入
5. 如果要根據分發結果排序，兩種方法: 
   a. 把第 114 行的 records.sort 註解打開 b. 在 excel 檔裡面，把 result 那欄根據升序 or 降序排列