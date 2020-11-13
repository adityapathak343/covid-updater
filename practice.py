l = int(input('Enter L\n>')) #lowercase_number
d = int(input('Enter D\n>')) #number_of_words
n = int(input('Enter N\n>')) #number_of_test_cases

lst = []

for _ in range(d):
    j = input('Enter Known Word\n>')
    for i in j:
        if i not in lst:
            lst.append(i)

lst += ['(', ')']
for _ in range(n):
    tc = input('TC>')
    is_valid = True
    poss_lst = []
    i = 0
    for _ in range(len(tc)):
        if tc[i] not in lst:
            is_valid = False
            break
        elif tc[i] == '(':
            new_tup = ()
            for k in range (i+1, len(tc)):
                if tc[k] == ')':
                    i = k
                    poss_lst.append(new_tup)
                    break
                elif tc[k] not in lst:
                    is_valid = False
                    break 
                else:
                    new_tup += tc[k],
        else:
            poss_lst.append((tc[i]))
        if i >= len(tc)-1:
            break
        else:
            i = i+1

    if len(poss_lst) != 3:
        is_valid = False
        fnum = 0

    if is_valid == True:
        flist = []
        for i in poss_lst:
            for j in i:
                print(i)    