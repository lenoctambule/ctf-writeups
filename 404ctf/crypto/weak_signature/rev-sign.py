

def sum_data(data):
    chksum = sum(data)
    return chksum

f1 = open("script.py.zsig", "rb")

data1 = f1.read()

sum_sample = sum_data(data1[312:])

f2 = open("payload.py", "rb")

data2 = f2.read()

sum_payload = sum_data(data2[:-1])
sum_diff = sum_sample - sum_payload
len_diff = len(data1[312:]) - len(data2[:-1])

print(f"sum_diff={sum_diff}, len_diff={len_diff}")
div = len_diff - 1
pad_char1 = (sum_diff - (sum_diff % div)) / div
pad_char2 = sum_diff % div
print(f"pc1 = {pad_char1}; pc2 = {pad_char2}")
print((pad_char1)*(len_diff-1)+pad_char2)
char1 = chr(int(pad_char1))
char2 = chr(int(pad_char2))

f3 = open("payload.py.zsig", "w+b")

f3.write(data1[:312])
f3.write(data2[:-1])
padding = char1*(len_diff-1)+char2
f3.write(padding.encode())
