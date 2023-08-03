## 功能

此為輔助在spine4.0版本前，實現外框線效果的圖片預處理工具
如果要在spine內實現外框線效果且不讓外框線粗細變形，可使用此預處裡工具。

spine 4.0以後的版本已經內建功能解決了此問題。

## 原由

由於外框圖片必須與本體圖片百分百同步變形，必須使外框圖片的mesh與本體圖片的mesh百分百相同，通常是由複製外框的mesh作為本體的mesh，但在3.8版本以前會有因圖片版面尺寸不同造成的拉扯問題。

在圖片零件量非常大的情況下手動處理會非常耗時。

## 解決

理論上只需要將本體圖片的版面尺寸擴大成與框線圖片的版面尺寸一樣即可。

## 使用步驟

A資料夾放置要被修改版面尺寸的圖片（本體）

B資料夾放置目標版面尺寸的圖片（外框線）

A資料夾是本體圖片，B資料夾是外框線的圖片
此程式可以自動把A資料夾的所有圖片改成對應的B資料夾的圖片的尺寸

ex：A1會被改成B1的尺寸,A2會被改成B2的尺寸

**重要條件：**
AB兩組圖片必須是**配對**的，例如A組有十張圖片，B也必須有十張圖片，且檔案名稱排序也必須相同，如下所示：

```
A:['03_boat_line.png', '03_brocade_a_line.png', '03_brocade_b_line.png', '03_coral_pink_line.png', '03_coral_red_line.png', '03_purplebag_line.png', '03_sail_line.png']

B:['03_boat_light.png', '03_brocade_a_light.png', '03_brocade_b_light.png', '03_coral_pink_light.png', '03_coral_red_light.png', '03_purplebag_light.png', '03_sail_light.png']
```
兩組圖片的每一個配對放在同一個版面內的時候，中心點應是相同的，
否則出來的圖片會有偏移誤差
