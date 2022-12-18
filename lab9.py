import random
import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a")


k = int(input("Vvedite kol-vo popytok:"))
logging.info(f"Users entered: {k}")
n = int(input("Vvedite granitcu dlya chisla:"))
logging.info(f"Users entered: {n}")

i = random.randint(1,n)
logging.info(f"Randomed number is: {i}")
logging.info("The game was started")
while i != 0:
    a = int(input("Try your luck:"))
    logging.info(f"Users tries: {a}")
    if a > i:
        print("Slishkom mnogo")
        k -= 1
    if a < i:
        print("Slishkom malo")
        k -= 1
    if a == i:
        print("Congratulations, you were right!")
        logging.info("User wons!")
        break
    if k == 0:
        print("No more attempts try again.")
        logging.info("User lose!")
        break