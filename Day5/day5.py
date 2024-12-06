# Puzzle 1

# file_object=open(r"./day5.txt", 'r')
# arr=file_object.read()
# rule, order=arr.split('\n\n')
# rule=rule.split()
# order=order.split()
# midSum=0
# for i in range(len(order)):

#     orderCheck=order[i].split(',')

#     for j in range(len(orderCheck)-1):

#         flag=0

#         for k in range(j+1, len(orderCheck)):

#             if orderCheck[j]==orderCheck[k]:
#                 continue
#             checkStr=orderCheck[j]+'|'+orderCheck[k]  
#             if checkStr not in rule:
#                 flag+=1
#                 break

#         if flag!=0:
#             break

#     else:
#         midSum=midSum+int(orderCheck[int(len(orderCheck)/2)])
    

# print(midSum)

# Puzzle 2

file_object=open(r"./day5.txt",'r')
arr=file_object.read()
rule, order=arr.split('\n\n')
rule=rule.split()
order=order.split()
midSum=0
for i in range(len(order)):

    orderCheck=order[i].split(',')
    flag=0
    for j in range(len(orderCheck)-1):

        for k in range(j+1, len(orderCheck)):

            if orderCheck[j]==orderCheck[k]:
                continue
            checkStr=orderCheck[j]+'|'+orderCheck[k]  
            if checkStr not in rule:
                flag+=1
                orderCheck[j],orderCheck[k]=orderCheck[k],orderCheck[j]
    if(flag!=0):
        midSum+=int(orderCheck[int(len(orderCheck)/2)])            
    
print(midSum)