def IP_replacement(input_txt):
    """
    初始置换IP
    """
    ip_table = [2, 6, 3, 1, 4, 8, 5, 7]
    output_txt = []
    for i in range(len(ip_table)):
        output_txt.append(input_txt[ip_table[i] - 1])
    return output_txt


def spilt_txt(input_txt):
    """
    划分左右子部分
    """
    left_txt = []
    right_txt = []
    left_txt = input_txt[:4]
    right_txt = input_txt[4:]
    return left_txt, right_txt


def extended_permutation(input_txt):
    """
    扩展置换
    """
    ep_box = [4, 1, 2, 3, 2, 3, 4, 1]
    output_txt = []
    for i in range(len(ep_box)):
        output_txt.append(input_txt[ep_box[i] - 1])
    return output_txt


def wheel_key(input_txt, ki):
    """
    加轮密钥
    """
    output_txt = []
    for i in range(len(input_txt)):
        output_txt.append(input_txt[i] ^ ki[i])
    return output_txt


def s_boxs_1(input_txt):
    """
    替换盒1
    """
    row = input_txt[0] << 1 | input_txt[3]
    column = input_txt[1] << 1 | input_txt[2]
    s_box_1 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 0, 2]]
    output = s_box_1[row][column]
    output_txt = []
    output_txt.append(output >> 1)
    output_txt.append(output & 1)
    return output_txt


def s_boxs_2(input_txt):
    """
    替换盒2
    """
    row = input_txt[0] << 1 | input_txt[3]
    column = input_txt[1] << 1 | input_txt[2]
    s_box_2 = [[0, 1, 2, 3], [2, 3, 1, 0], [3, 0, 1, 2], [2, 1, 0, 3]]
    output = s_box_2[row][column]
    output_txt = []
    output_txt.append(output >> 1)
    output_txt.append(output & 1)
    return output_txt


def direct_replacement(input_txt):
    """
    直接置换
    """
    SPBox = [2, 4, 3, 1]
    output_txt = []
    for i in range(len(SPBox)):
        output_txt.append(input_txt[SPBox[i] - 1])
    return output_txt


def generation_secret_key(secret_key):
    """
    子密钥生成
    """
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    left_shift_1 = [2, 3, 4, 5, 1]
    left_shift_2 = [2, 3, 4, 5, 1]
    middle_txt = []
    for i in range(len(P10)):
        middle_txt.append(secret_key[P10[i] - 1])
    left_txt = middle_txt[:5]
    right_txt = middle_txt[5:]
    left_output_1 = []
    right_output_1 = []
    for i in range(len(left_shift_1)):
        left_output_1.append(left_txt[left_shift_1[i] - 1])
    for i in range(len(left_shift_1)):
        right_output_1.append(right_txt[left_shift_1[i] - 1])
    middle_txt.clear()
    middle_txt = left_output_1 + right_output_1
    k1 = []
    for i in range(len(P8)):
        k1.append(middle_txt[P8[i] - 1])
    left_output_2 = []
    right_output_2 = []
    for i in range(len(left_shift_2)):
        left_output_2.append(left_output_1[left_shift_2[i] - 1])
    for i in range(len(left_shift_2)):
        right_output_2.append(right_output_1[left_shift_2[i] - 1])
    middle_txt.clear()
    middle_txt = left_output_2 + right_output_2
    k2 = []
    for i in range(len(P8)):
        k2.append(middle_txt[P8[i] - 1])
    return k1, k2


def F(input_txt, k, x):
    """轮函数F"""
    middle_txt = extended_permutation(input_txt)
    middle_txt = wheel_key(middle_txt, k)
    middle_txt_left = middle_txt[:4]
    middle_txt_right = middle_txt[4:]
    if x == 1:
        middle_txt_left = s_boxs_1(middle_txt_left)
        middle_txt_right = s_boxs_2(middle_txt_right)
    else:
        middle_txt_left = s_boxs_1(middle_txt_left)
        middle_txt_right = s_boxs_2(middle_txt_right)
    middle_txt.clear()
    middle_txt = middle_txt_left + middle_txt_right
    output_txt = direct_replacement(middle_txt)
    return output_txt


def xor(input_txt, xor_txt):
    """异或"""
    middle_txt = []
    for i in range(len(input_txt)):
        middle_txt.append(input_txt[i] ^ xor_txt[i])
    return middle_txt


def IP_replacement_inverse(input_txt):
    """
    最终置换IP
    """
    ip_table = [4, 1, 3, 5, 7, 2, 8, 6]
    output_txt = []
    for i in range(len(ip_table)):
        output_txt.append(input_txt[ip_table[i] - 1])
    return output_txt


def main_encryption(plain_txt, k):
    """
    加密算法
    """
    middle_txt = IP_replacement(plain_txt)
    left_txt, right_txt = spilt_txt(middle_txt)
    k1, k2 = generation_secret_key(k)
    # print(k1)
    # print(k2)
    xor_txt = F(right_txt, k1, 1)
    left_txt = xor(left_txt, xor_txt)
    left_txt, right_txt = right_txt, left_txt
    xor_txt.clear()
    xor_txt = F(right_txt, k2, 2)
    left_txt = xor(left_txt, xor_txt)
    middle_txt.clear()
    middle_txt = left_txt + right_txt
    cypher_txt = IP_replacement_inverse(middle_txt)
    return cypher_txt


def main_decryption(cypher_txt, k):
    """
    解密算法
    """
    middle_txt = IP_replacement(cypher_txt)
    left_txt, right_txt = spilt_txt(middle_txt)
    k1, k2 = generation_secret_key(k)
    xor_txt = F(right_txt, k2, 2)
    left_txt = xor(left_txt, xor_txt)
    left_txt, right_txt = right_txt, left_txt
    xor_txt.clear()
    xor_txt = F(right_txt, k1, 1)
    left_txt = xor(left_txt, xor_txt)
    middle_txt.clear()
    middle_txt = left_txt + right_txt
    plain_txt = IP_replacement_inverse(middle_txt)
    return plain_txt


if __name__ == '__main__':
<<<<<<< HEAD
    plain_txt = [1, 1, 1, 1, 0, 0, 0, 0]
=======
    plain_txt = [1, 0, 0, 1, 0, 0, 0, 0]
>>>>>>> 86cd9a2be8dab3453bc8698ebedc9f30ad3d520e
    k = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    cypher_txt = main_encryption(plain_txt, k)
    print(plain_txt)
    print(cypher_txt)
    print(main_decryption(cypher_txt, k))
