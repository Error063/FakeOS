def commandline(username):
    import os,threadmanager,time
    os.chdir(os.path.abspath(f"../data/users/{username}"))
    current_path=os.path.abspath(f"../data/users/{username}")
    while True:
        command=input(f"[ {username}@localhost {current_path} ]\n>>> ")
        if command=="":
            continue
        program_args=command.split()
        if program_args[0]== 'exit':break
        if program_args[0]== 'cd':
            os.chdir(os.path.abspath(program_args[-1]))
            current_path=os.path.abspath(program_args[-1])
            continue
        if program_args[0]== 'ls':
            if program_args[0]==program_args[-1]:
                for item in os.listdir("./"):
                    print(item)
            else:
                for item in os.listdir(os.path.abspath(program_args[-1])):
                    print(item)
            continue
        threadmanager.createThread(appList=program_args)
        time.sleep(0.1)
        continue