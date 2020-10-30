print('Hello, welcome to my home!')

ans = input('Are you ready to play (yes/no)?: ')
score = 0
total_q = 4

if ans.lower() == 'yes':
     ans = input('1. What is the best part of my home? ')
     if ans.lower() == 'the living room' or 'your room':
         score += 1
         print('Correct')
     else:
         print('Incorrect')

     ans = input('2. What is the name of my dog? ')
     if ans.lower() == 'rex':
         score += 1
         print('Correct')
     else:
         print('Incorrect')

     ans = input('3. How many rooms do I have? ')
     if ans == '3':
         score += 1
         print('Correct')
     else:
         print('Incorrect')

     ans = input('4. Do I have a pool inside of my home? ')
     if ans.lower() == 'yes':
         score += 1
         print('Correct')
     else:
         print('Incorrect')

     print('Thank you for playing, you got ', score, 'questions correct.')
     mark = (score/total_q) * 100

     print('Mark: ', str(mark) + '%')

print('Godbye!')