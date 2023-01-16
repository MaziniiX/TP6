def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

lst1=[0,1,2]
lst2=ajouter_elt(lst1,3)
print(lst1)
print("type =",type(lst1))
print("ID =%d"%id(lst1))
print()
print(lst2)
print("type =",type(lst2))
print("ID =%d"%id(lst2))