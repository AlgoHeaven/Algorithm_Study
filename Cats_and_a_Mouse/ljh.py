def catAndMouse(x, y, z):
    if abs(z-x)==abs(z-y):
        return "Mouse C"
    elif abs(z-x)>abs(z-y):
        return "Cat B"
    else:
        return "Cat A"

x,y,z = map(int,input.split())
print(catAndMouse(x,y,z))