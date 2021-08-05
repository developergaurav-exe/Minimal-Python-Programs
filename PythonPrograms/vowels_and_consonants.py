str=input('Enter a Character: ').upper()
vowel=0
consonant=0
for i in str:
                if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                                        vowel=vowel+1
                else:
                                consonant=consonant+1
                
                
print('Number of vowel is=',vowel)
print('Number of consonant is=',consonant)
