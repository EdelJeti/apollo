import time

with open('kangaroosong.txt') as f:

    for zeile in f: 
        print(zeile)
        time.sleep(1)