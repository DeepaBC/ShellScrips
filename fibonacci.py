num=int(input("enter number:"))
i=0
fn=0
sn=1
while(i<num):
        if(i<=1):
                next=i
        else:
                next=fn+sn
                fn=sn
                sn=next
        print(next)
        i=i+1
