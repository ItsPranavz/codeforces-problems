inputs = []
list = [i for i in "codeforces"]
for i in range(int(input())):
  inputs.append(input())
for char in inputs:
  if char.lower() in list:
    print("YES")
  else:
    print("NO")
