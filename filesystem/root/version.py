def app(list):
    import platform,osinfo
    print(f'FakeOS {osinfo.osVersion} Build {osinfo.osBuild}')
    print('===Host Information===')
    print(f'Host:{platform.system()} {platform.release()}')
    print(f'Host Platform:{platform.machine()}')
    print('===Python Runtime Information===')
    print(f'Python implementation:{platform.python_implementation()}')
    print(f'Python version:{platform.python_version()}')
    print(f'Python branch:{platform.python_branch()}')
    print(f'Python compiler:{platform.python_compiler()}')
    print(f'Python revision:{platform.python_revision()}')
