v1, v2, v3, v4, v5 = "a", "e", "i", "o", "u"
v1n, v2n, v3n, v4n, v5n = 0, 0, 0, 0, 0
word = input()
flag1 = True
flag2 = True
flag3 = True
vowels = [v1, v2, v3, v4, v5]

for i in range(len(word)):
  if word[i] == "a":
      v1n += 1
  elif word[i] == "e":
      v2n += 1
  elif word[i] == "i":
      v3n += 1
  elif word[i] == "o":
      v4n += 1
  elif word[i] == "u":
      v5n += 1

vowelnum = [v1n, v2n, v3n, v4n, v5n]

for i in range(len(vowelnum)-1):
  if vowelnum[i] < vowelnum[i+1]:
      flag1 = False
      break

vowel_position = {"a": -1, "e": -1, "i": -1, 'o': -1, 'u': -1}
for key in vowel_position:
  for j in range(len(word)):
    if word[j] == key:
      vowel_position[key] = j
      break

keys1 = list(vowel_position.values())
for i in range(len(keys1)-1):
  if keys1[i] > keys1[i+1]:
      flag2 = False
      break

for i in range(len(vowelnum)):
  if vowelnum[i] == 0:
      flag3 = False
      break
  

if (flag1 and flag2 and flag3):
  print("It is a perfect word")
else:
  print("It is not a perfect word")
