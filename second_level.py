import time
import math

start = time.time()

for subsetID in range(32):

    f = open("32files/subset"+str(subsetID)+".txt", "r")
    contents = f.readlines()
    f2 = open("5letterwords.txt", "r")
    c2 = f2.readlines()

    max_entropy = 0
    max_word = ""
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
            subid = ""
            subid = subid.join(str1)
            subset = int(subid, 2)
            dict [subset] += 1

        # sum = 0
        # for key in dict.keys():
        #    sum += dict[key]

        for key in dict.keys():
            dict[key] = dict[key]/len(contents)

        entropy = 0
        for key in dict.keys():
            if dict[key] != 0:
                entropy += -1 * (math.log(dict[key])*dict[key])

        if max_entropy < entropy:
            max_entropy = entropy
            max_word = inp_word
    print(f"Subset ID: {subsetID}")
    print(f"Max entropy is for word {max_word}: {max_entropy}")
    # print(f"List of intersections for each subset: {dc}")

    

end = time.time()

print(f"Time taken: {end - start}")

"""
OUTPUT:
Subset ID: 0
Max entropy is for word CULTY: 3.0347330780575157
Subset ID: 1
Max entropy is for word MULCT: 2.6558253189426817
Subset ID: 2
Max entropy is for word CUNDY: 2.7651465272546045
Subset ID: 3
Max entropy is for word BUNDT: 2.3462729346192157
Subset ID: 4
Max entropy is for word CYTON: 2.968968130991956
Subset ID: 5
Max entropy is for word PLONK: 2.509181365456566
Subset ID: 6
Max entropy is for word COUNT: 2.611868024416311
Subset ID: 7
Max entropy is for word THONG: 2.041409183240232
Subset ID: 8
Max entropy is for word LOUND: 2.9480367849812548
Subset ID: 9
Max entropy is for word POULT: 2.56062205274982
Subset ID: 10
Max entropy is for word DONUT: 2.543867202521209
Subset ID: 11
Max entropy is for word POUTY: 1.9926793411314159
Subset ID: 12
Max entropy is for word BLOND: 2.5478566686306525
Subset ID: 13
Max entropy is for word PLANT: 1.8999897568085082
Subset ID: 14
Max entropy is for word BUNDT: 1.8013628783945568
Subset ID: 15
Max entropy is for word COMPT: 1.136467501320835
Subset ID: 16
Max entropy is for word OCTYL: 2.869354023437986
Subset ID: 17
Max entropy is for word CLOTH: 2.4789754878499424
Subset ID: 18
Max entropy is for word OCTYL: 2.5830957530373024
Subset ID: 19
Max entropy is for word PUNTO: 1.9866776088885796
Subset ID: 20
Max entropy is for word PLONG: 2.4324377611811876
Subset ID: 21
Max entropy is for word PLONK: 1.9532041031315277
Subset ID: 22
Max entropy is for word MULCT: 1.8916535946393525
Subset ID: 23
Max entropy is for word BLUNT: 1.3641966783078654
Subset ID: 24
Max entropy is for word BLOND: 2.4200178762347724
Subset ID: 25
Max entropy is for word BLUNT: 1.8941404729227946
Subset ID: 26
Max entropy is for word MULCT: 1.7462116859553682
Subset ID: 27
Max entropy is for word PLUCK: 1.122910533635662
Subset ID: 28
Max entropy is for word CLINT: 1.9283163351426071
Subset ID: 29
Max entropy is for word BLAND: 1.3208883431493221
Subset ID: 30
Max entropy is for word DUMPY: 1.4058647484570574
Subset ID: 31
Max entropy is for word : 0
Time taken: 220.4751262664795
"""