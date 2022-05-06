import json
import time

f = open("5letterwords.txt", "r")

contents = f.readlines()

f.close()

start = time.time()
oneInter = {}

for i in range(65, 91):
    key = chr(i)
    oneInter[key] = 0
    for line in contents:
        word = line.strip()
        if chr(i) in word:
            oneInter[key] += 1

with open("1letter.json", "w") as f:
    json.dump(oneInter, f)

end = time.time()

print(f"Time taken to calculate one letter intersections: {end-start} seconds")
print(f"Number of keys: {len(oneInter.keys())}")
one = end - start

start = time.time()

twoInter = {}

for i in range(65, 91):
    for j in range(i+1, 91):
        key = chr(i) + chr(j)
        twoInter[key] = 0
        for line in contents:
            word = line.strip()
            if chr(i) in word and chr(j) in word:
                twoInter[key] += 1

with open("2letter.json", "w") as f:
    json.dump(twoInter, f)

end = time.time()

print(f"Time taken to calculate two letter intersections: {end-start} seconds")
print(f"Number of keys: {len(twoInter.keys())}")
two = end - start

start = time.time()

threeInter = {}

for i in range(65, 91):
    for j in range(i+1, 91):
        for k in range(j+1, 91):
            key = chr(i) + chr(j) + chr(k)
            threeInter[key] = 0
            for line in contents:
                word = line.strip()
                if chr(i) in word and chr(j) in word and chr(k) in word:
                    threeInter[key] += 1

with open("3letter.json", "w") as f:
    json.dump(threeInter, f)

end = time.time()
three = end - start
print(f"Time taken to calculate three letter intersections: {three} seconds")
print(f"Number of keys: {len(threeInter.keys())}")
print(f"Total time: {one+two+three} seconds")