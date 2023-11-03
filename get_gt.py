import sys
import os
import numpy as np

categorys = ["car", "taxi", "bus", "minibus"]
keys = {0: "car", 1: "taxi", 2: "bus", 3: "minibus"}

# categorys = ["car", "truck", "bus", "motor", "bike"]
# keys = {0: "car", 1: "truck", 2: "bus", 3: "motor", 4: "bike"}

image_ids = open('test_hk.txt') 

if not os.path.exists("./input"):
    os.makedirs("./input")
if not os.path.exists("./input/ground-truth"):
    os.makedirs("./input/ground-truth")
 
i = 0
while i < 100000:
    line = image_ids.readline().strip().split()
    img_na = line[1].split("\\")
    if img_na[-1][0:-4] == 'img00208':
        cc = 1
    
    f = open("./input/ground-truth/" + img_na[-1][0:-4] + ".txt","w")
    num_obj = len(line) - 2
    for j in np.arange(num_obj):
        obj = line[j + 2]
        obj = obj.split(',')
        obj_name = str(keys[int(obj[4])])
        left = obj[0]
        top = obj[1]
        right = obj[2]
        bottom = obj[3]
        f.write("%s %s %s %s %s\n" % (obj_name, left, top, right, bottom))
    f.close()
    i += 1


print("Conversion completed!")
