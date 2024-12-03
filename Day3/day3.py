# Puzzle one

# def findSum(n_index, i, arr, n1, n2, sum):
#     if(not arr[n_index].isdigit()):
#         i=n_index+1
#         return i, sum
#     while arr[n_index].isdigit():
#         n1+=arr[n_index]
#         n_index+=1
#     n_index+=1
#     if(not arr[n_index].isdigit()):
#         i=n_index+1
#         return i, sum
#     while arr[n_index].isdigit():
#         n2+=arr[n_index]
#         n_index+=1
#     if(not arr[n_index]==')'):
#         i=n_index+1
#         return i, sum
#     sum+=int(n1)*int(n2)
#     i=n_index+1
#     return i, sum

# file_object=open(r"./day3.txt", 'r')
# arr=file_object.read()
# sum=0
# i=0
# while i<len(arr):
#     i=arr.find('mul(', i)
#     if(i==-1):
#         break
#     n_index=i+4
#     n1=''
#     n2=''
#     (i, sum)=findSum(n_index, i, arr, n1, n2, sum)
    
# print(sum)

# Puzzle 2

def findSum(n_index, i, arr, n1, n2, sum):
    if(not arr[n_index].isdigit()):
        i=n_index+1
        return i, sum
    while arr[n_index].isdigit():
        n1+=arr[n_index]
        n_index+=1
    n_index+=1
    if(not arr[n_index].isdigit()):
        i=n_index+1
        return i, sum
    while arr[n_index].isdigit():
        n2+=arr[n_index]
        n_index+=1
    if(not arr[n_index]==')'):
        i=n_index+1
        return i, sum
    sum+=int(n1)*int(n2)
    i=n_index+1
    return i, sum

file_object=open(r"./day3.txt", 'r')
arr=file_object.read()
str_check='mul('  
sum=0
i=0
while i<len(arr):
    dont=arr.find('don\'t()', i)
    while i<dont:
        check=i+1 # when there is no mul( then find will return -1. In order to change that a variable check is used
        i=arr.find('mul(', i)
        if(i>dont):
            break
        elif(i==-1):
            i=check
            break
        n_index=i+4
        n1=''
        n2=''
        (i, sum)=findSum(n_index, i, arr, n1, n2, sum)
    i=arr.find('do()', i)
    if(i==-1):
        break
     
print(sum)