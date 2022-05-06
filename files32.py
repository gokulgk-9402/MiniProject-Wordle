import string
import time

start = time.time()

f = open("5letterwords.txt", "r")
contents = f.readlines()
f.close()

max_wd = "AESIR"
sorted = "AEIRS"
dict = {}

for word in contents:
    word = word.strip()
    ls = []
    str1 = []
    for i in range(5):
        if sorted[i] in word:
            str1.append('1')
        else:
            str1.append('0')

    setid = ""
    setid = setid.join(str1)
    subset = str(int(setid,2))

    if subset in dict.keys():
        dict[subset] += 1
    else:
        dict[subset] = 1

    f = open("subset"+subset+".txt", 'a')
    f.write(word+'\n')
    f.close()

end = time.time()

print(f"Wrote 32 files!\nTime taken: {end-start}")
print("List of intersections:")

for i in range(32):
    print(f"{i}: {dict[str(i)]}")

"""
OUTPUT:
Wrote 32 files!
Time taken: 2.6129980087280273
List of intersections:
0: 597
1: 916
2: 295
3: 303
4: 553
5: 531
6: 187
7: 160
8: 917
9: 928
10: 581
11: 341
12: 424
13: 293
14: 241
15: 89
16: 868
17: 925
18: 457
19: 331
20: 361
21: 251
22: 173
23: 56
24: 600
25: 444
26: 407
27: 131
28: 66
29: 16
30: 32
31: 4
"""