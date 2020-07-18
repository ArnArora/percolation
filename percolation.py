import random
##0=blocked, 1 = open
##make a graph of n by n

def create_ids(n):
    list1 = [i for i in range(n**2)]
    list1.append(n**2)
    list1.append(n**2+1)
    return list1

def create_grid(n):
    list1 = []
    for i in range(n):
        list2 = []
        for j in range(n):
            list2.append(0)
        list1.append(list2)
    return list1

def union(a,b, ids, n):
    ##first find the parent of a
    d = find_parent(a, ids, n)
    ##set the parent of a = b
    ids[d] = b
    return ids

def connected(a, b, ids, n):
    return find_parent(a, ids, n)==find_parent(b, ids, n) or ids[a]==ids[b]

def find_parent(a, ids, n):
    num = 0
    while ids[a]!= a and num<n**2:
        a=ids[a]
        num+=1
    return a

def get_id(r,c, n):
    return r*n+c

def open_list(list, n, ids):
    x = random.randint(0, n-1)
    y = random.randint(0,n-1)
    z = list
    z[x][y]=1
    ids = open_ids(x,y,z,n,ids)
    return list, ids
    
def open_ids(x,y,z,n,ids):
    if x==0:
        ids = union(y, n**2, ids, n)
    elif x==n-1:
        ids = union(get_id(x,y,n), n**2+1, ids, n)
    if x!=n-1 and z[x+1][y]==1:
        ids = union(get_id(x+1,y,n), get_id(x,y,n), ids, n)
    if y!=0 and z[x][y-1]==1:
        ids = union(get_id(x,y-1,n), get_id(x,y,n), ids, n)
    if y!=n-1 and z[x][y+1]==1:
        ids = union(get_id(x,y+1,n), get_id(x,y,n), ids, n)
    if x!=0 and z[x-1][y]==1:
        ids = union(get_id(x-1,y,n), get_id(x,y,n), ids, n)
    return ids
##check if the graph percolates
def isPercolate(list, n):
    return connected(n**2, n**2+1,list, n)

def openings(list, n):
    count = n**2
    for i in range(n):
        for j in range(n):
            if list[i][j]==0:
                count-=1
    return count

def main(n, t):
    sum = 0
    for i in range(t):
        x = create_grid(n)
        y = create_ids(n)
        while not isPercolate(y, n):
            x, y = open_list(x, n, y)
        count = openings(x, n)
        sum+= count/n**2
    return sum/t




