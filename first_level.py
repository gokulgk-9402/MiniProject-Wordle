import time
import math

start = time.time()

f = open("5letterwords.txt", "r")
contents = f.readlines()
c2 = contents

max_entropy = 0
max_word = "AAHED"
dc = {}

for input_word in c2:
    # inp_word = input("Enter a 5 letter word:")
    inp_word = input_word.strip()
    inp_list = list(inp_word)
    inp_set = set(inp_list)
    inp_distinct = list(inp_set)
    inp_distinct.sort()

    no = len(inp_distinct)

    dict = {}
    for i in range(2**no):
        dict[i] = 0

    for word in contents:
        w = word.strip()
        ls = []
        str1 = []
        for i in range(no):
            if inp_distinct[i] in w:
                str1.append('1')
            else:
                str1.append('0')
        str = ""
        str = str.join(str1)
        subset = int(str, 2)
        dict [subset] += 1

    # sum = 0
    # for key in dict.keys():
    #    sum += dict[key]
    tempd = dict.copy()

    for key in dict.keys():
        dict[key] = dict[key]/12478

    entropy = 0
    for key in dict.keys():
        if dict[key] != 0:
            entropy += -1 * (math.log(dict[key])*dict[key])

    if max_entropy < entropy:
        max_entropy = entropy
        max_word = inp_word
        dc = tempd.copy()

end = time.time()

print(f"Time taken: {end - start}")
print(f"Max entropy is for word {max_word}: {max_entropy}")
print(f"List of intersections for each subset: {dc}")

"""
OUTPUT:
Time taken: 229.9267909526825
Max entropy is for word AESIR: 3.1866554283772484
List of intersections for each subset: {0: 597, 1: 916, 2: 295, 3: 303, 4: 553, 5: 531, 6: 187, 7: 160, 8: 917, 9: 928, 10: 581, 11: 341, 12: 424, 13: 293, 14: 241, 15: 89, 16: 868, 17: 925, 18: 457, 19: 331, 20: 361, 21: 251, 22: 173, 23: 56, 24: 600, 25: 444, 26: 407, 27: 131, 28: 66, 29: 16, 30: 32, 31: 4}
"""
