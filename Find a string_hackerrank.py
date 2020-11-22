# https://www.hackerrank.com/challenges/find-a-string/problem
# Method - 1 (successful

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if len(sub_string) < len(string):
            if i <= (len(string) - len(sub_string)):
                if sub_string == string[i:i + len(sub_string)]:
                    count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


#Method-2 [failure]
def count_substring(string, sub_string):
    count = 0
    myindex = string.find(sub_string)
    # print(myindex)
    nextindex = myindex + 1
    # print(nextindex)
    count = count + 1
    while myindex+len(sub_string) < len(string):
        myindex = string.find(sub_string, nextindex, len(string))
        nextindex = myindex + 1
        count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


#Method-3 [ successful]

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        # print("Hello1")
        if string.startswith(sub_string, i):
            # print("Hello2")
            count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)