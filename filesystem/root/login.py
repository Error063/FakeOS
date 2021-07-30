def login():
    import hashlib, shelve,getpass
    username=input("Username:")
    password=input("Password:")
    if username=='' or password=='':
        print("Username or password error, try again")
        return None
    password_check=hashlib.sha256(password.encode('utf-8')).hexdigest()
    userdb=shelve.open("../data/system/main")
    for i in range(0,len(userdb["users"])):
        try:
            real_password=userdb["users"][i][username]
        except KeyError:
            continue
    if real_password==password_check:
        return username
        userdb.close()
    else:
        print("Username or password error, try again")