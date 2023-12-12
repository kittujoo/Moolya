import re


def create_A_to_Z_list():
    A_to_Z_list = [chr(i) for i in range(ord('a'), ord('z'))]
    print(A_to_Z_list)
    return A_to_Z_list


def create_1_to_26_list():
    A_to_Z_list = [ascii(i) for i in range((1), (27))]
    print(A_to_Z_list)
    return A_to_Z_list


if __name__ == '__main__':
    create_A_to_Z_list()
    create_1_to_26_list()
    # re.split('')

    p = {'a':1,'b':2,'c':3,'d':4}
    sum=0
    str_sum = 'bc'
    for i in p:
        if i in str_sum:
            print('p[i] : ',p[i])
            sum= sum+p[i]
            print('sum : ',sum)