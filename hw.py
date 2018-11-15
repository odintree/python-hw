#FIRST PART

#1
""" def shape(a): 
    print(len(a), len(a[1]))

shape([[1, 2, 3], [4, 5, 6]])


#2
m = [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]
pos = (1, 1)
def print_map(m, pos):
    for y, elems in enumerate(m):
        for x, k in enumerate(elems):
            if x == pos[0] and y == pos[1]:
                print("@", end='')
                continue
            if k == 0:
                print("#", end='')
            elif k == 1:
                print(".", end='')
        print()
    
    
print_map(m, pos) """


#SECOND PART
#1
def hamming(s1,s2):
    count=0
    for a, b in zip(s1, s2):
        if(a != b):
            count += 1
    return (count)
s1 = "abc"
s2 = "abd"
hamming(s1, s2)

#2 
def hba1(path, hamming):
    firsttwo = []
    f=open(path)
        for i in range(N):
            line=f.next().strip()
            firsttwo.append(line)
        f.close()

    with open (path) as thefile:
        shortest = hamming
        pair = ()
        for line in thefile:
            hamming()
