lucky_numbers = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]
number_input = int(input())
is_true = False
for n in lucky_numbers:
    if number_input % n == 0:
      is_true = True
      break
    else:
        pass
if is_true:
    print("YES")
else:
    print("NO")
