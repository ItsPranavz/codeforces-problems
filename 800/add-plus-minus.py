for i in range(int(input())): 
    n = int(input())
    s = input()
    sum = s[0] == '1'
    for i in range(1, n):
        if s[i] == '0' :
            print('+', end = "")
        elif sum:
            print('-', end = "")
            sum = 0
        else :
            print('+', end = "")
            sum = 1
    print()
