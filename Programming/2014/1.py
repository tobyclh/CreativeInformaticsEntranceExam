count = 0
with open('out1.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        count += len(line) - len(line.replace('|',''))
print(f'Count of | : {count}')