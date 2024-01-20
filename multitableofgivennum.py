fh=open('output9.txt','w')
n=int(input('enter the number:'))
for i in range(1,11):
    print(n,'x',i,'=',n*i)
    fh.write(f'multiplication table of a given number {n} is {n,'x',i,'=',n*i} \n')
fh.close()