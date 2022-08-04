#Dictionaries and Maps

n = int(input())
name_number= {}
for i in range(n):
    s = input().rstrip().split()
    name_number[s[0]] = s[1]

s = "b"
while s != "":
    try:
        s = input()
        if s not in name_number.keys():
            print("Not found")
        else:
            print(s + "=" + name_number[s])
    except EOFError:
        break
