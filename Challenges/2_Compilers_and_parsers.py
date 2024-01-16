n = int(input())

for _ in range(n):
    ml = 0
    d = 0
    for i, c in enumerate(input()):
        if c == '>':
            if d == 1:
                d = 0
                ml = i + 1
            elif d > 1:
                d -= 1
            else:
                break
        else:
            d += 1
    print(ml)


'''
n=int(input())
for i in range(n):
    ma=0
    st=[]
    s=[j for j in input()]
    for j in range(len(s)):
        #print(j,end='')
        if(s[j]=='<'):
            st.append(s[j])
        elif(s[j]=='>' and len(st)!=0):
            #print(st)
            st.pop()
            if(len(st)==0):
                ma=j 
        else:
            break
    if(ma!=0):
        ma+=1
    print(ma) 
'''