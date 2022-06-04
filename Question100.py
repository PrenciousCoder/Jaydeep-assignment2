
"""def palindrome(checklist):
    if len(checklist) < 1:
        return True
    else:
        if checklist[0] == checklist[-1]:
            return palindrome(checklist[1:-1])
        else:
            return False"""
    




from audioop import reverse
import re


def FilterPalindrome(checklist)->list:
    for string in checklist:
        print(string)
        #rev_string=reverse(str(string))
        rev_string=''.join(reversed(str(string)))
        print(rev_string)
        find_num=checklist.count(rev_string)
        if find_num>0:
            print("(",string,",",rev_string,")")
        else:
            continue


FilterPalindrome([93,24,42,66])
#assert FilterPalindrome([93,24,42,66]) ==[(24,42),(66)]

