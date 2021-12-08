def corresponding_parenthesis(text):
    one = 0
    two = 0
    for i in text:
        if i == ")":
            one += 1
        else:
            two += 1
    if(one>two):
        return ")" * (one - two)
    elif(one<two):
        return "(" * (two - one)
    else:
        return ""

def remove_more_than_two_repetitions(text):
    res = ""
    for i in range(len(text)):
        if(text[i - 2] != text[i] or text[i - 1] != text[i]):
            res += text[i]
    return res