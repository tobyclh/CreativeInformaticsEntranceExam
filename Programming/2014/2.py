with open('out1.txt','r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'main' in line:
            print(f'Line {i+1} : {line[:-1]}')