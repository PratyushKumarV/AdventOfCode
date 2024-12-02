# Puzzle one

# def isSafe(l):
#     diff=int(l[0])-int(l[1])
#     if not 1<=abs(diff)<=3: 
#             return False
#     elif diff>0:   # Values are decreasing
#         for i in range(1, len(l)-1):
#             d=int(l[i])-int(l[i+1])
#             if d<=0 or abs(d)>3:
#                 return False
#     else:   #values are increasing
#         for i in range(1, len(l)-1):
#             d=int(l[i+1])-int(l[i])
#             if d<=0 or abs(d)>3:
#                  return False
#     return True
     
# file_object=open(r"./day2.txt", 'r')
# arr=file_object.readlines()
# safeCount=0
# for i in range(len(arr)):
#     if isSafe(arr[i].split()):
#          safeCount+=1
# print(safeCount)

# Puzzle two

def isSafe(l):
    diff=int(l[0])-int(l[1])
    if not 1<=abs(diff)<=3: 
            return False
    elif diff>0:   # Values are decreasing
        for i in range(1, len(l)-1):
            d=int(l[i])-int(l[i+1])
            if d<=0 or abs(d)>3:
                return False
    else:   #values are increasing
        for i in range(1, len(l)-1):
            d=int(l[i+1])-int(l[i])
            if d<=0 or abs(d)>3:
                 return False
    return True

def isSafe2(l):
    for i in range(len(l)):
        k=l[:i]+l[i+1:]
        if isSafe(k):
           return True
    return False
     

file_object=open(r"./day2.txt", 'r')
arr=file_object.readlines()
safeCount=0
for i in range(len(arr)):
    if isSafe(arr[i].split()):
         safeCount+=1
    elif isSafe2(arr[i].split()):
         safeCount+=1
print(safeCount)