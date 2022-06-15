def processString(String: str) -> str:
    num=len(String)
    temp=''
    for i in range (0,num):
        if String[i]=='(' or String[i]=='[' or String[i]=='{':
            temp=temp+String[0:i]
            break 
    for i in range(num-1,-1,-1):
        if String[i]==')' or String[i]==']' or String[i]=='}':
            temp=temp+String[i+1:num]
            break 
    return(temp)

print(processString('abcd [ab{c} dd'))