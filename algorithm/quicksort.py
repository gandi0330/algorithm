def quicksort(arr):

    if len(arr) > 1:
        key = arr[0]

        front, end = 1, len(arr) - 1
        while front < end:
            k1 = 0
            k2 = 0
            if key >= arr[front] : 
                front += 1
            else :
                k1 = 1

            if key <= arr[end] :
                end -= 1
            else:
                k2 = 1
            
            if k1 and k2 :
                arr[front], arr[end] = arr[end], arr[front]
            
        

    else:
        pass

