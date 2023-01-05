list =  [5,7,44,55,64,86,100,101,98]

n = int(input("enter the value you want to search:"))

pos = -1

def search(list, n):
    l = 0
    u = len(list)-1

    for i in range(len(list)):
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
             
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False

if search(list, n):
    print("found at position", pos)
else:
    print("not found")