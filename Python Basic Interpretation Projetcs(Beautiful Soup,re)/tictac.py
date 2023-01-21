def main():
    a=input(" Do You Want to Play (Yes/NO) ? ")
    if a=='yes' or a=='Yes':
        a=True
        b=input("choose your symbol (X or O) First Player")
        while(a==True):
            
            if b=='X' or b=='x':
                sym='O'
                a=move(b,sym)
            elif b=='o' or b=='O':
                b='O'
                sym='X'
                a=move(b,sym)
            else:
                print(" Wrong Symbol Choose Again (X or O)")
                a=True
        
    else:
        exit()



def move(b,sym):
    lst0 = ['','','']
    lst1 = ['','','']
    lst2 = ['','','']
    c=True
    chala=2
    l=3
    while c:
        disp(lst0,lst1,lst2)
        if chala%2==0:
            m=int(input(f"Enter Position Number Player First ({b}) "))
        else:
            m=int(input(f"Enter Position Number Player Second ({sym}) "))
        
        if(0<m<4 and ):
            m=m-1
            if chala%2==0:
                lst0[m]=b
                chala=chala+1
            else:
                lst0[m]=sym
                chala=chala+1
            l=len(lst0)-1
            c=check(lst0,lst1,lst2)
        elif 3<m<6:
            m=m%3-1
            if chala%2==0:
                lst1[m]=b
                chala=chala+1
            else:
                lst1[m]=sym
                chala=chala+1
            c=check(lst0,lst1,lst2)
        elif m==6:
            m=2
            if chala%2==0:
                lst1[m]=b
                chala=chala+1
            else:
                lst1[m]=sym
                chala=chala+1
            c=check(lst0,lst1,lst2)
        elif 6<m<9:
            m=m%3-1
            if chala%2==0:
                lst2[m]=b
                chala=chala+1
            else:
                lst2[m]=sym
                chala=chala+1
            c=check(lst0,lst1,lst2)
        elif m==9:
            m=2
            if chala%2==0:
                lst2[m]=b
                chala=chala+1
            else:
                lst2[m]=sym
                chala=chala+1
            c=check(lst0,lst1,lst2)
        else:
            print("Enter correct choice (1-9)")
    if c==False:
        
        ip=input(" Wanna Play Again ?\t")
        if(ip=="yes" or ip=="Yes"):
            return True   
        else: return False
    disp(lst0,lst1,lst2)


        

def disp(lst0,lst1,lst2):
    print("\n TicTac Board \n")
    print(f'\t{lst0[0]} ||'+f'  {lst0[1]}  ||'+f' {lst0[2]}')
    print('\t==============')
    print(f'\t{lst1[0]} ||'+f'  {lst1[1]}  ||'+f' {lst1[2]}')
    print('\t==============')
    print(f'\t{lst2[0]} ||'+f'  {lst2[1]}  ||'+f' {lst2[2]}')
    print('\n')

def check(lst0,lst1,lst2):
    i=j=k=0
    if lst0==lst1 or lst1==lst2 or lst0==lst2: return True
        
    elif lst0[i]==lst0[i+1]==lst0[i+2] or lst1[i]==lst1[i+1]==lst1[i+2] or lst2[i]==lst2[i+1]==lst2[i+2] or lst0[i]==lst1[i]==lst2[i] or lst0[i+1]==lst1[i+1]==lst2[i+1] or lst0[i+2]==lst1[i+2]==lst2[i+2] or lst0[i]==lst1[i+1]==lst2[i+2] or lst2[i]==lst1[i+1]==lst0[i] :
        disp(lst0,lst1,lst2)
        print("\n You Won \n")
        return False
    else:
        return True


    
main()