# Created variable to store the phrase 

phrase=('Welcome our channel!')

'''This is a name block'''

Name= input('Please enter your name : ')
Title= input('What is your title please? ')

'''This is a gender block'''

if Title == 'mr,MR,Mr':
    print(' Welcome here ' + Title + ' ' + Name + ' , How are you Mister?')
elif Title == 'miss,MISS,Miss,ms,MS,Ms,MRS,mrs,Mrs':
    print(' Welcome here ' + Title + ' '  + Name + ' , How are you Mylady today?')
else:
    print(' Welcome here ' + Title + ' ' + Name + ' , How are you, dude?')
