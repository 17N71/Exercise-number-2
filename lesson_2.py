# list1 = ['534545','abc','xyz',"ff"]
# listOfNumber = '1234567890'
# newlist = []
# def sameSum(list1):
#     try:
#         for i in list1:
#             for k in i:
#                 pass
#             for j in listOfNumber:
#                 if k in j and int(i[0]) == int(i[-1]):
#                     newlist.append(int(k))
#         if newlist[0] == newlist[-1]:
#             print(newlist[0] + newlist[-1])
#     except:
#             print("not same")
# # sameSum(list1)
# # First exercise 1 variant
# list2 = ['abc','xyz',"ff",'1223']
# listLast = list2[-1]
# if int(listLast[0]) == int(listLast[-1]):
#     print(int(listLast[0]) + int(listLast[-1]))
# else:
#     print("not same or number not in last index")

# # First exercise 2 variant

# listWithDublicates = [66, 4, "a", "bc", "bc", "a", "d", 4]
# newList = list(set(listWithDublicates))
# print(newList)

# # Second exercise

# listToEmpty = []
# if len(listToEmpty) == 0:
#     print("List is empty")
# else:
#     print("list isn't empty")

# # Third exercise

# def ff():
#     try:
#         e = int(input("Enter index to searching in list: "))
#         listToSearch = [33, "asda", 111, 66]
#         lengInList = len(listToSearch)
#         print(listToSearch[e])
#     except IndexError:
#         print("Sorry your number big then list length:")
#         print("try again:")
#         ff()
#     except ValueError:
#         print("Please write a number")
#         ff()
# ff()

# # fourth exercise

# firstDir = {
#     'x':3,
#     'y':6,
#     'z':4,
# }
# dictLo = dict(sorted(firstDir.items(), key=lambda x: x[1]))
# print(dictLo)
# # Five exercise

# exampleDict = {
    # "firstKey":"firstValue",
    # "secondKey":"secondValue",
    # "thirdKey":"thirdValue"
# }
# dictNameOfKey = input("enter name of key: ")
# if dictNameOfKey in exampleDict:
    # exampleDict.pop(dictNameOfKey) # variant 1
    # del exampleDict[dictNameOfKey] #variant 2
# print(exampleDict)
## six exercise
# searchInDict = input("Enter name of key: ")
# exampleDictTwo = {
#     "firstKey":"firstValue",
#     "secondKey":"secondValue",
#     "thirdKey":"thirdValue"
# }
# if  searchInDict in exampleDictTwo:
#     print(True)
# else:
#     print(False)
## seven exercise