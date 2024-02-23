word=input()
flag=True
flag2=True
if len(word)<8 or len(word)>32:
  flag2=False
  
for i in range(len(word)):
  if flag2==False:
    break
  if ord(word[0]) not in range(65,91) or ord(word[0]) not in range(97,123):
    flag=False
    break
  if word[i]=="/" or  word[i]=="\\" or word[i]=="'":
    flag=False
    break
  if word[i]=="\"" or  word[i]==" "  or word[i]=="=":
    flag=False
    break

if flag and flag2:
  print("True")
else:
  print("False")

    
    