def is_isogram(string):

    # brute force
    c = 'abcdefghijklmnopqrstuvwxyz'
    s = string.lower()
    check = sum([s.count(l) > 1 for l in s if l in c]) < 1
    return bool(check)