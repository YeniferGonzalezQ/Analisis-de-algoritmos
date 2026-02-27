n = int(input()) #Stones in row
st = input() #string s

stones = 0 #Stones to remove

for i in range(1, len(st)):
    if st[i] == st [i-1]: #compare if the neighbor before is equals
        stones += 1  #if it is, +1 to the stones to remove

print(stones)
