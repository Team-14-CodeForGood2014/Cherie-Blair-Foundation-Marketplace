import hashlib

while 1:

    inputString = raw_input("Enter the password: ")

    print hashlib.sha224(inputString).hexdigest()
