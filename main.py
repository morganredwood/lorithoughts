print("The dog used to potty inside on a potty pad.")
print("You want your dog to only go outside now.")
print("Does the dog have to potty?")
potty = input("y or n and press Enter: ")
while True:
    if potty == 'y':
        print("Do you take the dog outside?")
        outside = input("y or n and press Enter: ")
        if outside == 'y':
            print("The dog goes potty outside.")
            print("Hooray for you.")
            break
        elif outside == 'n':
            print("Is the floor clear?")
            clear = input('y or n and press Enter: ')
            while True:
                if clear == 'y':
                    print("The dog waits.")
                    print("Later, the dog still has to potty.")
                    print("Do you take the dog outside?")
                    outside = input("y or n and press Enter: ")
                    while True:
                        if outside == 'y':
                            print("The dog goes potty outside.")
                            print("Hooray for you.")
                            break
                        elif outside == 'n':
                            print("The dog can't wait.")
                            print("The dog goes potty inside.")
                            print("Clean up the pee.")
                            break
                        else:
                            print("Do you take the dog outside?")
                            outside = input("y or n and press Enter: ")
                            continue
                    break
                elif clear == 'n':
                    print("The dog is confused.")
                    print("The dog goes potty inside.")
                    print("Clean up the pee.")
                    break
                else:
                    print("Is the floor clear?")
                    clear = input('y or n and press Enter: ')
                    continue
        else:
            print("Do you take the dog outside?")
            outside = input("y or n and press Enter: ")
            continue
        break
    elif potty == 'n':
        break
    else:
        print("Does the dog have to potty?")
        potty = input('y or n and press Enter: ')
        continue
print("Go do something else.")
print("The End")
