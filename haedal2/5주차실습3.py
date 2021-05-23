'''
print("# read 이용")
with open("new.txt", 'r') as f:
    data = f.read()
    print(data)
    '''

'''
print("# readline 이용")
with open("new.txt",'r') as f:
    while True:
        line = f.readline()
        if not line: break
        print(line)
        '''


print("# readlines 이용")
with open("new.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
