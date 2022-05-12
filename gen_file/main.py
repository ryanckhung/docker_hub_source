import os
import time

WAIT_FOR_SECOND = 10

counter = 0
os.system("mkdir data -p")
os.system("cd data")

while True:
    try:
        cmd = 'echo "Hello {}" > ./data/{}.txt'.format(counter,counter)
        os.system(cmd)
        counter = counter + 1
        time.sleep(WAIT_FOR_SECOND)
    except:
        print("error")


