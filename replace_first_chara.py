"""
s=input('enter first value:')
chr=s[0]
s=s.replace(chr,'&')
final = chr+s[1:]
print(final)
"""
main_string = input("Type a string : ")
char = main_string[0]
main_string = main_string.replace(char,'$')
print(char+main_string[1:])
