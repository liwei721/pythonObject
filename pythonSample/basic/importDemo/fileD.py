import dis

test = open('fileC.py').read()
co = compile(test, 'fileC.py', 'exec')
dis.dis(co)