d1={'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
print(d1)
num=input('Enter the number in digits')
ans=""
for key in num:
                value=d1[key]
                ans=ans+value+""
print('The number',num,'in words is',ans)
