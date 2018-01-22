yours=['Yale','MIT','Berkeley']
mine=['Yale','Berkeley','HKUST']
ours1=mine+yours
ours2=[]
ours2.append(mine)
ours2.append(yours)
print(ours1)
print(ours2)
yours[1]="Harvard"
print(ours1)
print(ours2)


print("ANSWER: ours1 is an independent list, while ours2 depends on the definitions of yours and mine.")
