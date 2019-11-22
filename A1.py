import pandas as pd     #importing pandas
df=pd.DataFrame(index=['RECURRING EXPENSES','UNSEEN EXPENSES','CHILDREN EDUCATION EXPENSES',
                       'COMMUNICATION EXPENSES','FUEL EXPENSES','ITEM EXPENSES'],columns=['PRICE'])
sal=int(input(('ENTER YOUR SALARY:')))       #extracting data from the user
re=int(input('RECURRING EXPENSES:'))
ue=int(input("UNSEEN EXPENSES:"))
cee=int(input('CHILDREN EDUCATION EXPENSES:'))
ce=int(input("COMMUNICATION EXPENSES:"))
fe=int(input('FUEL EXPENSES:'))
it=int(input('TOTAL ITEMS EXPENSES:'))
ans=(input(('WANT TO ADD EXTRA EXPENSES(Y/N):')))
if ans=='Y' or ans=='y':
    l=[]
    n=int(input('HOW MANY EXPENSES:'))
    for i in range(0,n):
        ex=input('ENTER THE CATEGORY OF EXPENSE')
        cce=int(input('ENTER THE CORRESPONDING EXPENSE'))
        l.append(ex)
        df.loc[ex]=[cce]
df.iloc[0,0]=re
df.iloc[1,0]=ue
df.iloc[2,0]=cee
df.iloc[3,0]=ce
df.iloc[4,0]=fe
df.iloc[5,0]=it
a=1                                                     #updating the data
ans=input('DO U WANT TO UPDATE YOUR EXPENSES(Y/N):')
while a:
    if ans=='Y' or ans=='y':
        x=input('WHICH EXPENSE DO U WANT TO UPDATE:')
        y=int(input('ENTER THE NEW EXPENSE'))
        df.loc[x]=y
        ans1=input(('DO YOU WANT TO UPDATE MORE(Y/N):'))
        if ans1=='N'or ans1=='n':
            a=0
    else:
        a=0
df.loc['TOTAL EXPENSE']=df['PRICE'].sum()
print('YOUR CSV FILE OF EXPENSE IS AS FOLLOWS:')    #displaying the data
df.to_csv('expense1.csv')#saving the csv
print('--------------------------------------------------------------')
print(df)
print('--------------------------------------------------------------')
te=df.iloc[-1,0]                                #dispalying the slip
if sal-te>0:
    print('YOU HAVE SAVED',sal-te,'$')
else:
    print('YOU HAVE AN EXTRA EXPENDITURE OF ','$',te-sal)
