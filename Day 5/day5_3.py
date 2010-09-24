num =raw_input("Enter any 4 digit num:")

data = list(num)
output=[]
for key, value in enumerate(data[::-1]):
    value = int(value)
    if key%2!=0:
        digit = value * 2
        if digit > 10:
            value = digit %10 + digit/10
    output.append(value)

if sum(output)%10 == 0:
    print "valid"
else:
    print "invalid"