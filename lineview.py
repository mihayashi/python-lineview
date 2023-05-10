import os,sys, csv

#引数が３つであることを確認
if len(sys.argv)!=3:
    print("使い方：lineview.py ファイル名 行番号")
    sys.exit()
#表示元のファイルが存在することを確認する
in_file = sys.argv[1]
if not os.path.exists(in_file):
    print("ファイルが存在しません")
    sys.exit()

#行番号
line_no = int(sys.argv[2])
print("line_no: ", line_no)

i = 1

with open(in_file,"r", newline="", encoding="utf_16") as in_f:
    for line in in_f:
        if line_no == i :
            print(line)
            break
        i += 1
        
