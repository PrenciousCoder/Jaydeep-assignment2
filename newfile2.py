def isPerfect(n) -> bool:
    sum = 0                             # initialise sum
    list_div = [1]              # adding 1 directly to list because exception to the method
    for i in range(1, n):             # 1 to num - 1, since we want proper divisors
        if n / i in range(1, n):    # because all divisors come in pairs, so if it is in that range, it is a divisor
            list_div.append(i)  # this list gives all proper divisors

    for i in list_div:
        sum += i                        # takes sum to check if that equals num
    if sum == n:
        return True                     # boolean output

    else:
        return False
if __name__ == "_main_":
    assert isPerfect(6) == True
    assert isPerfect(22) == False
    assert isPerfect(28) == True
    assert isPerfect(496) == True