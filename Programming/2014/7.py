with open('out1.txt','r') as f:
    lines = f.readlines()
    previous_line = None
    duplicated_lines = 0
    for i, line in enumerate(lines):
        if line == previous_line:
            duplicated_lines += 1
        else:
            if duplicated_lines >= 3:
                print(previous_line[:-1])
            duplicated_lines = 0
        previous_line = line
