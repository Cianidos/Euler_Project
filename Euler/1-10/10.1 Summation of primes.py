def primes(n):
    if n % 2 == 0:
        n += 1
    prime_nums = [] #пустой список куда мы будем добавлять простые числа
    primes = [True] * n #список Булевых значений, наши зачеркивания
    primes[0], primes[1] = [None] * 2 #0 и 1 заранее не простые
    for ind, val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            prime_nums.append(ind)
        elif val is True:
            primes[ind * 2::ind] = [False] * \
                 (((n - 1) // ind) - 1)
            prime_nums.append(ind)

    return prime_nums

nums = primes(2*10**6) #получаем список
print(nums[10001]) #выводим 10001 число
print(sum(nums)) #выводим сумму