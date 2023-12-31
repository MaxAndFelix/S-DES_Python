import threading
import time

import encrypt

lock = threading.Semaphore(value=0)
possible_key_list = []
secret_key_list = []
check_over = False


def number_to_list(n) -> list:
    output_list = []
    for i in range(10):
        t = n & 1
        n = n >> 1
        output_list.insert(0, t)
    return output_list


def brute_force_attack(s, plaintxt, cyphertxt, n):
    while s < 1024:
        secret_key = number_to_list(s)
        s = s + n
        cypher_txt = encrypt.main_encryption(plaintxt, secret_key)
        if cypher_txt == cyphertxt:
            possible_key_list.append(secret_key)
            lock.release()
    if s == 1024:
        lock.release()
    return


def secret_key_check(plaintxt, cyphertxt):
    """
    测试secret_key是否能满足一切明密文对照
    """
    global possible_key_list
    while 1:
        lock.acquire()
        if len(possible_key_list) == 0:
            return
        secret_key = possible_key_list[0]
        possible_key_list = possible_key_list[1:]
        check = 0
        for i in range(len(plaintxt)):
            plain_txt = plaintxt[i]
            cypher_txt = cyphertxt[i]
            plain_txt_check = encrypt.main_encryption(plain_txt, secret_key)
            if plain_txt_check == cypher_txt:
                continue
            else:
                check = 1
                break
        if check == 0:
            secret_key_list.append(secret_key)


def main_brute_force_attack(n, plaintxt, cyphertxt):
    """
    暴力破解主程序
    """
    secret_key_list.clear()
    start_time = time.time()
    Thread_check = threading.Thread(target=secret_key_check, args=(plaintxt, cyphertxt))
    Thread_check.start()
    for i in range(len(plaintxt)):
        plain_txt = plaintxt[i]
        cypher_txt = cyphertxt[i]
        Thread = threading.Thread(target=brute_force_attack, args=(i, plain_txt, cypher_txt, n))
        Thread.start()
    Thread_check.join()
    end_time = time.time()
    return secret_key_list, end_time - start_time


if __name__ == '__main__':
    print(main_brute_force_attack(1, [[1, 1, 0, 0, 1, 1, 0, 0]], [[1, 0, 0, 1, 0, 1, 0, 1]]))
