此為輔助在spine內實現外框線效果的圖片預處理工具
如果要在spine內實現外框線效果且不讓外框線粗細變形，可使用此預處裡工具


A資料夾放置要被修改版面尺寸的圖片

B資料夾放置目標版面尺寸的圖片

例如:A資料夾是本體,B資料夾是外框線的圖片
此程式可以自動把A資料夾的所有圖片改成對應的B資料夾的圖片的尺寸
ex:A1會被改成B1的尺寸,A2會被改成B2的尺寸

重要條件:
AB兩組圖片必須是配對的,例如A組有十張圖片,B也必須有十張圖片,且檔案名稱排序也必須相同,如下所示:

A:['03_boat_line.png', '03_brocade_a_line.png', '03_brocade_b_line.png', '03_coral_pink_line.png', '03_coral_red_line.png', '03_purplebag_line.png', '03_sail_line.png']
B:['03_boat_light.png', '03_brocade_a_light.png', '03_brocade_b_light.png', '03_coral_pink_light.png', '03_coral_red_light.png', '03_purplebag_light.png', '03_sail_light.png']

兩組圖片的每一個配對放在同一個版面內的時候,中心點應是相同的,
否則出來的圖片會有偏移誤差
