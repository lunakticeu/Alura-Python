def str_replace(text,ch):
    result = ''
    for i in text: 
            if i == ' ': 
                i = ch  
            result += i 
    return result

text = "l vey u"
ch = "o"

print(str_replace(text,ch))