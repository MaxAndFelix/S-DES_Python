def IP_replacement(input_txt):
    '''
    初始置换IP
    '''
    ip_table = [2, 6, 3, 1, 4, 8, 5, 7]
    output_txt = []
    for i in range(ip_table):
        output_txt.append(input_txt[ip_table[i]])
    return output_txt

def spilt_txt(input_txt):
    '''
    划分左右子部分
    '''
    left_txt = []
    right_txt = []
    left_txt = input_txt[:4]
    right_txt = input_txt[4:]
    return left_txt, right_txt


def main_encryption(plain_txt):
    middle_txt = IP_replacement(plain_txt)
    left_txt, right_txt = spilt_txt(middle_txt)
    
