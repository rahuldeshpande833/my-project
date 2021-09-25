
lst = [2,3,4,5,6,7,8,9]
first_index = 0
last_index = len(lst)-1
num = int(input("Enter a number"))
while first_index<=last_index:
    mid = (first_index+last_index)//2 #0+7/2
    if num == lst[mid]:
        print(num,"is at",mid,"index")
        break
    elif num<lst[mid]:
        last_index = mid-1 #//last_index=2
    else:
            first_index = mid+1
            if first_index>last_index:
                print("element not found")
