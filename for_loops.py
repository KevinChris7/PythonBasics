
def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = base_num * result
    return result


print(raise_to_power(2, 3))


