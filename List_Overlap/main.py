a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
i = 0

while(i < len(a)):
    j = 0;
    isFound = False
    while(j < len(b) and not isFound):
        if(a[i] == b[j]):
            if(a[i] not in c):
                c.append(a[i]);
            isFound = True;
        j += 1;
    i += 1;

print(c);
    
