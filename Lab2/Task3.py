matrix = [[2,5,1], [4,5,7],[9,0,4]]
for i in matrix:
    print(i)
    increasing = True
    current = i[0]
    for j in i:
        if j < current:
            increasing = False
            break
        current = j

    if increasing:
        i.sort(reverse=True)
        break

print(matrix)

