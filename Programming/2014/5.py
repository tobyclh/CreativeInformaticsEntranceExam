def is_similar(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    str1 += max(len2 - len1, 0)*' '
    str2 += max(len1 - len2, 0)*' '
    diff = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            diff += 1
    if diff < 5:
        return True
    else:
        return False




with open('out1.txt','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            line_1, line_2 = lines[i].strip(), lines[j].strip()
            if len(line_1) < 20 or len(line_2) < 20:
                continue
            if is_similar(line_1, line_2):
                print('--------')
                print(line_1)
                print(line_2)
                # print('--------')