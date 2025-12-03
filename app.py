#triggering scan
#final test
# test with block setting
#testing
import os
import subprocess

"""
def process_request(user_input):
    print("Processing request...")
    
    # BAD: Unsafe command execution
    os.system("echo " + user_input)
    
    # GOOD: Safe printing
    print("User said: " + user_input)

"""
def process_request(user_input):
    subprocess.run(["echo", user_input], shell=False)
