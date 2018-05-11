import os
matches = []
for (dirname, dirshere, fileshere) in os.walk(r'C:\Users\malinovskiyri\PycharmProjects\PPE4'):
    for filename in fileshere:
        if filename.endswith('.py'):
            pathname = os.path.join(dirname, filename)
            try:
                if 'mimetypes' in open(pathname).read():
                    matches.append(pathname)
            except:
                continue
for name in matches:
    print(name)
