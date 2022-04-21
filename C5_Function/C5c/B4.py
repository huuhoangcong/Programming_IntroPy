def parposition(dx,dy,nx,ny,x,y):
    a = x//dx
    b = y//dy

    return nx*b+a+1

print(parposition(1,1,4,4,3.5,3.5))