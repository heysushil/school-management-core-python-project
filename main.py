# Ye main file hai yaha par hi sare code kiye gaye hain

# os libaryr for creating file and folder
import os

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

# Create new class fucntion:
def create_new_class(school_name):
    # get class name
    class_name = input('Enter new class name: ')
    # first add school name on school list file
    add_class_name = open('schools/' + school_name + '/class_list.txt', 'a')
    add_class_name.write('\n'+class_name)
    add_class_name.close()
    # school_name se hi folder create karna hai
    os.mkdir('schools/'+ school_name + '/' + class_name)

    print('\nBadhai ho new class ' + class_name + ' create ho gaya hai.\n')

# Fucntion class choice ke liye
def class_choice(school_name):
    message = '''
    ---------------------------------
        School {0}
    ---------------------------------
    1. Create New Class
    2. Choose existing Class
    3. Exit
    ---------------------------------
    Only enter numbers:         
    '''.format(school_name)

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
            create_new_class(school_name)
        elif option == 2:
            print('\nChoose existing Class')
        elif option == 3:
            print('\nAap safalta purvak exit kar chuke hain.')
        else:
            print('\nAap ne galt input diya hai. Dubara sahi input choice ke sath try kare.')

# Create new school fucntion: Yaha par ek school ke name se folder create hoga. And school ka name ek school_list.txt file me addon bhi hoga.
def create_new_school():
    # get school name
    school_name = input('Enter new school name: ')
    # os path exists error check
    myfolderpath = 'schools/'+school_name
    if os.path.exists(myfolderpath):
        print('\nYe school ' + school_name + ' pahle se hi hai.\nYe sabhi existing schools ke name hain.\nInme se jis school me enter karna hai wo option input kariye?')
    else:
        # first add school name on school list file
        add_school_name = open('school_list.txt', 'a')
        add_school_name.write('\n'+school_name)
        add_school_name.close()

        # school_name se hi folder create karna hai
        os.mkdir('schools/'+school_name)

        print('\nBadhai ho new school ' + school_name + ' create ho gaya hai.\n')

        # New school create hone ke baad me class ke option ke fucniton ko call karna hai.
        class_choice(school_name)

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
