def sortLength(list):
    #uses insertion sorting with the name lengths to put them in the correct order
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j>=0 and len(key) < len(list[j]):
            list[j+1] = list[j]
            j = j-1

        list[j+1] = key
def exportArrayToFile(list):
    f = open("sorted.txt", "w")
    for i in list:
        f.write(i+"\n")
#Reads Names and places them in a List
with open("Sort Me.txt","r") as f:
    names = []
    for line in f:
        names.append(line.rstrip("\n"))

#Built in python to sort the names alphabetically, I dont want to reinvent the wheel
names.sort()
sortLength(names)
print(names)
exportArrayToFile(names)



