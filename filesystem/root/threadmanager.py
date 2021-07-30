import ctypes
import inspect
import launchup,shelve,threading,pprint
def _async_raise(tid, exctype):
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
def addThreadList(appname):
    threaddb=shelve.open("../../system/thread")
    threadNumber=threaddb["total"]
    threaddb["total"]=threadNumber+1
    threaddb["list"].update({threaddb["total"]:{"pid":threaddb["total"],"appName":appname,"status":"live"}})
    threaddb.sync()
    threaddb.close()
    return threadNumber+1
def createThread(appList):
    appName=appList[0]
    pid=str(addThreadList(appName))
    exec('program'+pid+"=threading.Thread(target=launchup.launchup, args="+str(appList)+")")
    exec("program"+pid+".start()")
def getThreadList(pid):
    threaddb = shelve.open("../../system/thread")
    if pid==None:
        pprint.pprint(threaddb["list"])
    else:
        try:
            pprint.pprint(threaddb["list"])
        except BaseException:
            print("Error pid")
    threaddb.close()
def killThread(pid):
    threaddb=shelve.open("../../system/thread")
    try:
        del threaddb["list"][pid]
    except BaseException:
        print("Error pid")
    else:
        threaddb["total"]+=1
        threaddb.sync()
        threaddb.close()
        eval("_async_raise("+"program"+str(pid)+".ident, SystemExit)")
def app(list):
    if list[1]=='get':
        if len(list)==2:
            getThreadList(None)
        else:
            getThreadList(list[2])
