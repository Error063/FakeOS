class RuntimeError(BaseException):
    pass

def launchup(*program_avgrs):
    try:
        launchapp="__import__('"+ str(program_avgrs[0]) + "').app("+str(program_avgrs)+")"
        exec(launchapp)
    except BaseException as e:
        raise RuntimeError(e)