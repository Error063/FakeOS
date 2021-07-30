def login():
    import hashlib, shelve
    username = input("Username:")
    password = input("Password:")
    if username == '' or password == '':
        print("Username or password error, try again")
        return None
    passwordCheck = hashlib.sha256(password.encode('utf-8')).hexdigest()
    userdb = shelve.open("../data/system/main")
    for i in range(0, len(userdb["users"])):
        try:
            realPassword = userdb["users"][i][username]
        except KeyError:
            continue
    if realPassword == passwordCheck:
        return username
        userdb.close()
    else:
        print("Username or password error, try again")


class info:
    appVersion = '0.0.1'
    appBuild = '1'
    appAuthor = 'Error063'
    appCompany = 'Example Company'
    createTime = 1627625284
