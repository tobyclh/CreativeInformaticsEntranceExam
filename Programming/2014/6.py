MAX_DIFF = 4
def is_similar(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    str1 += max(len2 - len1, 0)*' '
    str2 += max(len1 - len2, 0)*' '
    diff = 0
    should_skip = 0
    offset_1, offset_2 = 0, 0
    for i in range(max(len1, len2)):
        if diff > MAX_DIFF:
            return False
        char1, char2 = str1[i+offset_1], str2[i+offset_2]
        if char1 == char2:
            continue
        for j in range(MAX_DIFF - diff):
            if str2[i+offset_2+j] == char1:
                offset_2 += j
                diff += j
                continue
        for j in range(MAX_DIFF - diff):
            if str1[i+offset_1+j] == char2:
                offset_1 += j
                diff += j
                continue
            


        if char1 != char2:
            diff += 1
    if diff < MAX_DIFF:
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