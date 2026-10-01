def eh_multiplo(a,b): #quando tem true e false , é comum fazer is_multiple
    if a % b == 0: #se o resto for zero
        return True #posso deixar sem os returns e o else,que tambem daria o valor True ou False
    else:
        return False
eh_multiplo(7,3)