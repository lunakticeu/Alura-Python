def reverse_string(string):
    return string[::-1]


text = input('Enter a text to be reversed: ')
reversed_text = reverse_string(text)
print(reversed_text)