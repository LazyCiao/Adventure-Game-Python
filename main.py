name = input('Enter your name ')
print('Welcome', name, 'I will be your guide for this adventure. ')

answer = input('Are you ready to start? ').lower()

if answer == 'yes':
    print("Perfect, let's start... ")
    answer = input('You wake up in a strange room with no memory of how you got there. You have to find a way out and solve the mystery of your disappearance.\nYou decide to:\n1: go to the door.\n2: go to the window.\n3: go to the desk with a drawer.\nAnswer: ')
    if answer == '1':
        print('The door is locked. ')
        answer = input('Do you want to:\n1: Search the room for a key?\n2: Try to break the door?\nAnswer: ')
        if answer == '1':
            print('You find a key under the rug and use it to unlock the door ')
            print('Congratulations! You have escaped the room and discovered that you were kidnapped by a mad scientist who wanted to experiment on your memory.\nYou managed to escape just in time and bring the scientist to justice.\nThe end.')
        elif answer == '2':
            print('You trigger an alarm and get caught by the kidnapper.\nGame Over.')
        else:
            print('You have made too much noise and the kidnapper heard you.\nGame Over. ')
           
    elif answer == '2':
        print('The window is locked. ')
        answer = input('You decide to:\n1: Try to pick the lock and climb out of the window.\n2: Search the room for a tool to break the window.\nAnswer: ')
        if answer == '1':
            print('You successfully climb out of the window and escape, but never find out who the kidnapper was.\nThe end.')
        elif answer == '2':
            print('You find a hammer and use it to break the window.')
            print('Congratulations! You have escaped the room, but discover that you were on the top floor of a tall building.\nYou fall to your death.\nGame Over.')
        else:
            print('You have made too much noise and the kidnapper heard you.\nGame Over. ')

    elif answer == '3':
        print('You try to open the drawer.')
        print('The drawer is locked. ')
        answer = input('You decide to:\n1: Search the room for a key to unlock the drawer.\n2: Break open the drawer.\nAnswer: ')
        if answer == '1':
            print('You find a key and use it to unlock the drawer.')
            print('You find a note inside the drawer revealing that you were kidnapped by a criminal organization and were being held for ransom.\nYou managed to escape and call the police.\nThe end.')
        elif answer == '2':
            print('You try to break open the drawer but fail.')
            print('you trigger an alarm and get caught by the kidnapper.\nGame Over.')
        else:
            print('You have made too much noise and the kidnapper heard you.\nGame Over. ')

    else:
        print('You have made too much noise and the kidnapper heard you.\nGame Over. ')

elif answer == 'no':
    print('Come back when you are ready.')
else:
    print('Come back when you have an serious answer.')