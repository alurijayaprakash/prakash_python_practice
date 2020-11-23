# https://www.hackerrank.com/challenges/python-string-formatting/problem
def print_formatted(number):
    w = len(str(bin(number)).replace('0b', ''))
    for i in range(1,number+1):
        d2b = bin(i).replace("0b", "").rjust(w, ' ')
        d2o = oct(i)[2:].rjust(w, ' ')
        d2h = (hex(i)[2:]).upper().rjust(w, ' ')
        i = str(i).rjust(w, ' ')
        print (i, d2o, d2h, d2b)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)