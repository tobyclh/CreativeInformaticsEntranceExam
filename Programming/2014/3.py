with open('out1.txt','r') as f:
    lines = f.readlines()
    previous_line = None
    duplicated_lines = False    
    for i, line in enumerate(lines):
        if line == previous_line:
            duplicated_lines = True
        else:
            if duplicated_lines:
                print(previous_line[:-1])
            duplicated_lines = False
        previous_line = line
