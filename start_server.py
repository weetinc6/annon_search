import os
import time

#start Annon_search



def userAnswer(key_user_result) -> any:
    key_user_result = key_user_result
    time.sleep(3)
    return os.system("python main.py")



print("Welcome to Annon search")
print("Please wait...", end="\n")

key_user_result = input("Would like to start the server now: (Y / N)? ")
if(key_user_result == "Y"):
    userAnswer(key_user_result)
else:
    print("Unable to start server please check the script properly")


