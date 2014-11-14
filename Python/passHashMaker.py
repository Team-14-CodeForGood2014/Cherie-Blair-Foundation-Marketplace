while 1

    inputString = raw_input("Enter the password: ")

    hashlib.sha224(inputString).hexdigest()
