# Ye main file hai yaha par hi sare code kiye gaye hain

# again choice show karne ke liye function bana rahe hain
def choices():
    message = '''
    ---------------------------------
            Welcome Admin
    ---------------------------------
    1. Create New School
    2. Choose existing School
    3. Exit
    ---------------------------------
    Only enter numbers:         
    '''
    try:
        option = int(input(message))
    except ValueError:
        print('\nAap ne number ki jagah kuch aur input kiya hai. Kripya sahi input ke sath dubara try kare?')
    except NameError:
        print('\nAap ne alphabet input kiya hai jo ki galat hai. Sahi input ke sath dubara try kariye?')
    except:
        print('\nInput me koi problem aai hai. Kripya sahi input ke sath dubara try kare?')
    else:
        if option == 1:
            print('\nCreate New School')
        elif option == 2:
            print('\nChoose existing School')
        elif option == 3:
            print('\nAap safalta purvak exit kar chuke hain.')
        else:
            print('\nAap ne galt input diya hai. Dubara sahi input choice ke sath try kare.')

# Create new school fucntion: Yaha par ek school ke name se folder create hoga. And school ka name ek school_list.txt file me addon bhi hoga.
def create_new_school():
    print('\nCreate New School')

# Choose school fucntion: Yaha se existing school folder ke andar enter honge.
def choose_school():
    print('\nChoose school.')

# First 2 option admin ko dene hai
message = '''
---------------------------------
        Welcome Admin
---------------------------------
1. Create New School
2. Choose existing School
3. Exit
---------------------------------
Only enter numbers:         
'''
try:
    option = int(input(message))
except ValueError:
    print('\nAap ne number ki jagah kuch aur input kiya hai. Kripya sahi input ke sath dubara try kare?')
except NameError:
    print('\nAap ne alphabet input kiya hai jo ki galat hai. Sahi input ke sath dubara try kariye?')
except:
    print('\nInput me koi problem aai hai. Kripya sahi input ke sath dubara try kare?')
else:
    if option == 1:
        # print('\nCreate New School')
        create_new_school()
    elif option == 2:
        # print('\nChoose existing School')
        choose_school()
    elif option == 3:
        print('\nAap safalta purvak exit kar chuke hain.')
    else:
        print('\nAap ne galt input diya hai. Dubara sahi input choice ke sath try kare.')
