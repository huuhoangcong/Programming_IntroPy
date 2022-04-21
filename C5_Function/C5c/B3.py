def bbs(a):
    t = a[0]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            temp = a[i]
            if a[j]>a[i]:
                a[i]=a[j]
                a[j]=temp

    return a 

print(bbs([1,5,6,4,4,3,2]))