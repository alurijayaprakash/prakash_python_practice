# https://www.hackerrank.com/challenges/python-tuples/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    integer_tuple = tuple(map(int, input().split()))
    print(hash(integer_tuple))