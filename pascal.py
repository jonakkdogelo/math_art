
def fat(n):
    m = n if n != 0 else 1
    for i in range(1,n):
        m = m*i
    return m

def combi(n,p):
    c = fat(n)//(fat(n-p)*fat(p))
    return c

for i in range(11):
    tri = ''
    for j in range(i+1):
        tri += str(combi(i,j)) +' '
    print(tri)
        