given = "1 4 5 8 2 3 6 10 9 7"

splitted = given.split(" ")
even_list = []
odd_list = []

print splitted

for i in splitted:
    if (int(i)%2 == 0):
        even_list.append(i)
    else:
        odd_list.append(i)

even_list.reverse()
odd_list.sort()

output =odd_list + even_list
print output