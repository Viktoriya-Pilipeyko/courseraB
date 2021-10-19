dict_of_height = {'1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[], '10':[], '11':[]}
sum = 0
with open('dataset_3380_5.txt','r') as file:
    for line in file:
        list = line.split()
        dict_of_height[list[0]].append(list[2])

for value in dict_of_height:
    if dict_of_height[value] == []:
        print(value, '-')
    else:
        for i in dict_of_height[value]:
            sum += int(i)
        print(value, sum / len(dict_of_height[value]))
        sum = 0
