import os
import time
import random
import sys
if __name__ == '__main__':
    print(sys.argv[1])
    splitter = 2000000/20
    for l in range(997):
        for k in range(3):
            for j in range(10):
                for i in range(10):
                    os.system("python3 s.py " + str((3*l+k)*100 + splitter*(int(sys.argv[1])-1)))
                    time.sleep(random.randrange(0,3))
                time.sleep(random.randrange(1, 5))
            time.sleep(random.randrange(15, 20))
        time.sleep(random.randrange(15, 20))
