import time
import random

heads_or_tails = random.randint(0,1)
print("Flipping coin...")
time.sleep(2)
if heads_or_tails == 0:
    print("Heads")
elif heads_or_tails == 1:
    print("Tails")
else:
    print("Something went wrong.")