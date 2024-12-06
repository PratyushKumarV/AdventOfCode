# Puzzle 1

# def xmasCount(arr, count):
# # counting cases where XMAS or SAMX is present vertically
#     for i in range(len(arr)-3):
#         for j in range(len(arr[i])):
#             check=''
#             check=check+arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j]
#             if check=='XMAS' or check=='SAMX':
#                 count+=1

# # counting cases where XMAS and SAMX appear downwards diagonally moving towards the right            
#     for i in range(len(arr)-3):
#         for j in range(len(arr[i])-3):
#             check=''
#             check=check+arr[i][j]+arr[i+1][j+1]+arr[i+2][j+2]+arr[i+3][j+3]
#             if check=='XMAS' or check=='SAMX':
#                 count+=1

# # counting cases where XMAS and SAMX appear downwards diagonally moving towards the left
#     for i in range(len(arr)-3):
#         for j in range(len(arr[i])-3):
#             check=''
#             check=check+arr[i][j+3]+arr[i+1][j+2]+arr[i+2][j+1]+arr[i+3][j]
#             if check=='XMAS' or check=='SAMX':
#                 count+=1
#     return count

# file_object=open(r"./day4.txt")
# string=file_object.read()
# count=string.count("XMAS")+string.count("SAMX") # summing direct occurrences of XMAS and SAMX
# arr=string.split('\n')
# print(xmasCount(arr, count))

# Puzzle 2

file_object=open(r"./day4.txt", 'r')
arr=file_object.readlines()
count=0
for i in range(len(arr)-2):
    for j in range(len(arr[i].rstrip('\n'))-2):
        check1=''
        check2=''
        check1=check1+arr[i][j]+arr[i+1][j+1]+arr[i+2][j+2]
        check2=check2+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]
        con1=check1==check2=='MAS' or check1==check2=='SAM' # checking if both diagonals are the same
        con2=(check1=='MAS' and check2=='SAM') or (check1=='SAM' and check2=='MAS') # checking if both diagonals are different
        if(con1 or con2):
            count+=1
print(count)