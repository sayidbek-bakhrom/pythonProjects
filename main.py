def prime_number(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False

    if is_prime:
        return True
    else:
        return False


def prime_number_index(index):
    nums = []
    i = 2
    while len(nums) < index:
        if prime_number(i):
            nums.append(i)
        i += 1
    return nums[index-1]
  