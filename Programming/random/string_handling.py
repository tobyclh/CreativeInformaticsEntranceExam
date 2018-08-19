import difflib
text1 = 'I have a banana'
text2 = 'I have 2 bananas'

d = difflib.Differ()
diff = d.compare(text1, text2)
for _d in diff:
    print(_d)