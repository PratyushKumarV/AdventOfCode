# puzzle one

# file_object=open(r"./day1-puzzle1.txt", 'r')
# arr=file_object.readlines()
# i=0
# l_list=[]
# r_list=[]
# for i in range(len(arr)):
#     arr[i]=arr[i].split()
#     l_list+=[int(arr[i][0])]
#     r_list+=[int(arr[i][1])]
# for i in range(1, len(l_list)):
#     j=i-1
#     temp=l_list[i]
#     while(j>=0 and temp<l_list[j]):
#         l_list[j+1]=l_list[j]
#         j-=1
#     l_list[j+1]=temp
# for i in range(1, len(r_list)):
#     j=i-1
#     temp=r_list[i]
#     while(j>=0 and temp<r_list[j]):
#         r_list[j+1]=r_list[j]
#         j-=1
#     r_list[j+1]=temp
# dist=[]
# for i in range(len(l_list)):
#     dist+=[abs(r_list[i]-l_list[i])]
# file_object.close()
# print(sum(dist))

# puzzle 2
file_object=open(r"./day1-puzzle1.txt", 'r')
arr=file_object.readlines()
i=0
l_list=[]
r_list=[]
for i in range(len(arr)):
    arr[i]=arr[i].split()
    l_list+=[int(arr[i][0])]
    r_list+=[int(arr[i][1])]
for i in range(1, len(l_list)):
    j=i-1
    temp=l_list[i]
    while(j>=0 and temp<l_list[j]):
        l_list[j+1]=l_list[j]
        j-=1
    l_list[j+1]=temp
for i in range(1, len(r_list)):
    j=i-1
    temp=r_list[i]
    while(j>=0 and temp<r_list[j]):
        r_list[j+1]=r_list[j]
        j-=1
    r_list[j+1]=temp
sum=0
l_set=set(l_list)
for i in l_set:
    sum+=i*r_list.count(i)
print(sum)