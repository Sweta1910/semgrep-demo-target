#triggering scan
#final test
# test with block setting
#testing
import os

def process_request(user_input):
    print("Processing request...")
    
    # BAD: Unsafe command execution
    os.system("echo " + user_input)
    
    # GOOD: Safe printing
    print("User said: " + user_input)
    print("testing")
    print("changed secret and testing again")

def debug_mode():
    # BAD: Hardcoded secret for debugging
    api_key = "sk_live_1234567890abcdef"
    print(f"Connecting with {api_key}")
