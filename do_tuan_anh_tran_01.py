#Part one
#1
def shape(a): 
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
    


#3
def neighbours(m, pos):
    up = m[pos[0]][pos[1]-1]
    down = m[pos[0]][pos[1]+1]
    left = m[pos[0]-1][pos[1]]
    right = m[pos[0]+1][pos[1]]
    if (up == 1):
        print("(",pos[0],",",pos[1]-1,")")
    if (down == 1):
        print("(",pos[0],",",pos[1]+1,")")
    if (left == 1):
        print("(",pos[0]-1,",",pos[1],")")
    if (right == 1):
        print("(",pos[0]+1,",",pos[1],")")

#1.4
def find_route(m, initial):
    for x in range(initial[1],len(m[initial[0]])):
        print("(",initial[0],",",x,")")

#1.5
def escape(m, pos):
    row=0
    for i in m:
        colum=0
        for j in i:
            if (row == pos[0] and colum == pos[1]):
                print('@',end="")
            else:
                if(j==0):
                    print('#',end="")
                else:
                    print('.',end="")
            colum=colum+1
        print("\n")
        row=row+1
    for x in range(pos[1],len(m[1])-1):
        escape(m,(pos[0],x+1))

#2.1
def hamming(s1,s2):
    count=0
    for x in range(0,len(s1)-1):
        if(s1[x]==s2[x]):
            count += 1
    print(count)
s1 = "abacaba"
s2 = "abbccca"
hamming(s1, s2)

#2.2
def hba1(path, hamming):
    file = open("HBA1.txt", "r") # doesn't open ??
    lines = file.readlines()
    print(lines)

hba1_path = "HBA1.txt"
hba1(hba1_path,"s")


#3.1
dictionary = {}
def kmers(s, k):
    for i in range(0,len(s)-1):
        temp = ""
        for x in range(i,i+k):
            if(x>=i+k):
                break
            temp=temp+str(s[x])
        check(temp)
    print(dictionary)
def check(string):
    if string in dictionary:
        dictionary[string][0] = dictionary[string][0] + 1
    else:
        dictionary[string] = [1]

#3.2
def kmers(s, k):
    dictionary={}
    def check(string):
        if string in dictionary:
            dictionary[string][0] = dictionary[string][0] + 1
        else:
            dictionary[string] = [1]

    for i in range(0,len(s)-1):
        temp = ""
        for x in range(i,i+k):
            if(x>=i+k):
                break
            temp=temp+str(s[x])
        check(temp)
    return dictionary

def distance1(s1,s2):
    sum=0
    finaldict = {}
    dictionary1 = kmers(s1,2)
    dictionary2 = kmers(s2,2)
    print(dictionary1,"          ", dictionary2)
    if(len(dictionary1.keys())>=len(dictionary2.keys())):
        longdict=dictionary1
    else:
        longdict=dictionary2
    print(longdict)
    for x in longdict:
        if (x in dictionary1 and x in dictionary2):
            print("x ", x)
            print(dictionary1[x][0],"        ",dictionary2[x][0])
            sum += abs(dictionary1[x][0]-dictionary2[x][0])
        else:
            if (x in dictionary1):
                sum += abs(dictionary1[x][0])
            else:
                sum += abs(dictionary2[x][0])

    print(sum)

s1 = "abacaba"
s2 = "abracadabra"
distance1(s1, s2)