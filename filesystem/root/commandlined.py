def commandline(username):
    import os,threadmanager,time
    os.chdir(os.path.abspath(f"../data/users/{username}"))
    current_path=os.path.abspath(f"../data/users/{username}")
    while True:
        command=input(f"[ {username}@localhost {current_path} ]\n>>> ")
        if command=="":
            continue
        program_avgrs=command.split()
        if program_avgrs[0]=='exit':break
        if program_avgrs[0]=='cd':
            os.chdir(os.path.abspath(program_avgrs[-1]))
            current_path=os.path.abspath(program_avgrs[-1])
            continue
        if program_avgrs[0]=='ls':
            if program_avgrs[0]==program_avgrs[-1]:
                for item in os.listdir("./"):
                    print(item)
            else:
                for item in os.listdir(os.path.abspath(program_avgrs[-1])):
                    print(item)
            continue
        threadmanager.createThread(appList=program_avgrs)
        time.sleep(0.1)
        continue