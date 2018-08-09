with open('out1.txt','r') as f:
    lines = f.readlines()
    processed_lines = {}
    for i, line in enumerate(lines):
        line = line.strip()
        if line not in processed_lines.keys():
            processed_lines[line] = 1
        else:
            processed_lines[line] += 1
            print(f'Duplicated Line : {line}  / {processed_lines[line]}')