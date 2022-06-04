




def CheckItems(A,W,C)->list:
    item_list=[]
    Dict={}
    for i in range(0,len(A)):
        Dict[A[i]]=W[i]
    print(Dict)
    print(Dict.values())
    value=list(Dict.values())
    print(value)
    for j in range(0,len(W)):
        if value[j]<C:
            item_list.append(A[j])
        else:
            continue
    print(item_list)
    return item_list

CheckItems(["monkey","Elephant","Squirrel","cat"],[20,3000,0.4,5],50)
#assert CheckItems(["monkey","Elephant","Squirrel","cat"],[20,3000,0.4,5],50)== [["monkey","Squirrel","Cat"]]