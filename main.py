#1
#print(len(set(input().split())))

#2
#print(len(set(input().split()) & set(input().split())))

#3
#print(sorted(set(input().split()) & set(input().split()), key=float))

#4
a = input().split()
seen = set()
print('\n'.join(f'{x}: NO' if x not in seen and not seen.add(x) else f'{x}: YES' for x in a))

#5
