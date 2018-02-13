import os
print('echoenv...', end=' ')
try:
    print('Hello,', os.environ['USER'])
except:
    print('KeyError: \'USER\'')
