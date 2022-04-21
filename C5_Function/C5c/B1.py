def issym(a):
    count = 0
    for i in range(len(a)):
        if a[i]!=a[-i-1]:
            count+=1
    
    return True if count==0 else False


a = [5,4,3,2,1,5,3,4,5]
print(issym(a))