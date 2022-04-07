list = [1, 2, 3, 4, 5]

for i, val in enumerate(list):
    new_list = [val]
    if i > 0:
        for j in range(i+1, len(list)):
            new_list.append(list[j])
        for j in range(0, i):
            new_list.append(list[j])
    else:
        for j in range (i+1, len(list)):
            new_list.append(list[j])

    print(new_list)
