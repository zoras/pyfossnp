def generate_list():
    num_input = input("Enter the number you want to input in list:")
    data = []
    for i in range(0,num_input):
        list_entry = input("Enter the number in list:")
        data.append(list_entry)
    return data


def avarage(list):
    #list = [1,10,13]
    count = len(list)
    sum = 0
    for i in range(0,count):
            sum += list[i]
    avg = sum / count
    print "Average :",avg

def median(list):
    #list = [1,40,13,12,80,45]
    count = len(list)
    list.sort()
    print "Accending Sorted list: ", list
    if count%2==0:
        term = (count+1)/2
        median = (list[term-1] + list [term]) / 2.0
    else:
        term = (count+1)/2 -1
        median = list[term]   
    print "Median :",median

data = generate_list()
avarage(data)
median(data)


