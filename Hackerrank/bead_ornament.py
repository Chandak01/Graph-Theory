T=input()
for a in range(T):
    N=input()
    b=[int(next) for next in raw_input().split(' ')]
    ans = sum(b)
    ans = ans**(N-2)
    for x in b:
        ans*=x**(x-1)
    #ans*=sum(b)**(N-2)
    print int(ans)%1000000007