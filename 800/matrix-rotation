answers = []
for i in range(int(input())):
    a,b = map(int,input().split(" "))
    c,d = map(int,input().split(" "))
    is_true = False
    for j in range(4):
        if a<b and c<d and a<c and b<d:
            is_true = True
            break
        else:
            a,b,c,d = c,a,d,b
    if is_true:
      answers.append("YES")
    else:
      answers.append("NO")
for answer in answers:
  print(answer)
