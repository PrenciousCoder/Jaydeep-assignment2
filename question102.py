import numpy as np

def MatrixToSlab(matrix,m)->list:
    n=len(matrix)
    flat_list = [item for sublist in matrix for item in sublist]
    remain_m=len(flat_list)-m
    first_list=[]
    rem_list=[]
    for ele in matrix:
        for i in range(0,m):
            first_list.append(ele[i])
            
        arr=np.array(first_list)
        arr_2d=np.reshape(n,m)
    
    for ele2 in matrix:
        for j in range(m+1,remain_m+1):
            rem_list.append(ele2[j])
        arr2=np.array(rem_list)
        arr2_2d=np.reshape(n,remain_m)
    
    return arr_2d,arr2_2d

