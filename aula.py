def funcaoX(a):							
    if a % 2 == 1:						
        return 1						
    else:								
        return 2

def funcaoY(s):
    return len(s)


x = 10
print( funcaoX(x) + funcaoY("Terra") + x )