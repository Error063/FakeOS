import login,commandlined,shelve

threaddb=shelve.open("../data/system/thread")
threaddb["list"]={}
threaddb['total']=0
threaddb.sync()
threaddb.close()

debug=True
if not debug:
    username=None
    print("Welcome to use FakeOS alpha 0.0.1\nWhen you want to exit, please type 'exit' to exit, not click 'X' on the window.\n")
    while username==None:
        username=login.login()
else:
    username='root'
    print("Welcome to use FakeOS alpha 0.0.1\nDebug Mode:True\nWhen you want to exit, please type 'exit' to exit, not click 'X' on the window.\n")

commandlined.commandline(username)

threaddb=shelve.open("../../system/thread")
threaddb["list"]={}
threaddb['total']=0
threaddb.sync()
threaddb.close()