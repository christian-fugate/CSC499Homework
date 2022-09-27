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
notValid = True
while notValid:
    val = input("Would you like your Sort to be Reversed? Y/N \n")
    if val.lower() == 'y' or val.lower() == 'n':
        notValid = False
    else:
        print("You entered a invalid Response, Please Type either a 'Y' or a 'N'\n")
print(val)
if val.lower() == 'y':
    names.reverse()
    print(names) #Names should be sorted Reverse
else:
    print(names) #names should be sorted Normally

#I could get rid of the Else statment and move the print in line 34 out, but for the purposes of this
#   It looks better and reads better to have them both in the if else statements.
exportArrayToFile(names)



