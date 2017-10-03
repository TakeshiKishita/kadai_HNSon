def make_divisor_list(x):
    if x < 1:
        return []
    elif x == 1:
        return [1]
    else:
        divisor_list = []
        divisor_list.append(1)
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                divisor_list.append(i)
        divisor_list.append(x)

        return divisor_list