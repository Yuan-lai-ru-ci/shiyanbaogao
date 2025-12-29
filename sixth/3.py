def is_prime(n):
    """判断一个数是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_mersenne_primes(count):
    """寻找指定数量的梅森素数"""
    mersenne_primes = []
    p = 2  # 从最小的素数指数p开始
    while len(mersenne_primes) < count:
        if is_prime(p):
            m = 2**p - 1
            if is_prime(m):
                mersenne_primes.append(m)
                print(f"找到一个梅森素数: M = 2^{p} - 1 = {m}")
        p += 1
    return mersenne_primes

if __name__ == "__main__":
    print("开始寻找前 5 个梅森素数...")
    found_primes = find_mersenne_primes(5)
    print("\n前 5 个梅森素数是:", found_primes)
