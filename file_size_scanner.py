#Windows File は権限の問題でスキャン不可
import os, sys
files = os.listdir()
file_size = {}
file_size_list = []

for file in files:
    file_size[file] = round((os.path.getsize(file) / 1024) / 1024, 2)
    file_size_list.append(round((os.path.getsize(file) / 1024) / 1024, 0))

for k, v in sorted(file_size.items(), key=lambda x: -x[1]):
    print(str(k) + ": " + str(v) + " MB")

print()
print(os.getcwd() + 'の総消費容量は ' + str(sum(file_size_list)) + " MBです。")
