import random
compList = ['R', 'P', 'S']
#here the computer random the list
newcompList = random.choice(compList)
print 'Comp choice:', newcompList
#here you put your choice
inp = raw_input ('Choose R for "Rock", S for "Scissors", or P for "Paper" ')
print 'Your choice is:', inp
#here the if loop
if inp == newcompList:
    print 'Tie'
    
elif inp == 'R' and newcompList == 'S':
    print 'You win!'
    
elif inp == 'R' and newcompList == 'P':
    print 'You lose!'
    
elif inp == 'S' and newcompList == 'R':
    print 'You lose!'
    
elif inp == 'S' and newcompList == 'P':
    print 'You win!'
    
elif inp == 'P' and newcompList == 'R':
    print 'You win!'
    
elif inp == 'P' and newcompList == 'S':
    print 'You lose!'

else:
    print '==========='
    print ' Wrong!(}:/'
    print '==========='
#here a messenge to finish the game    
print '=========='
print 'Game over!'
