# Ye main file hai yaha par hi sare code kiye gaye hain

# os libaryr for creating file and folder
import os
import students_related_work as student

# again choice show karne ke liye function bana rahe hain
def school_choices():
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
            create_new_school()
        elif option == 2:
            choose_school()
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

# Class choose:
def choose_class(school_name):
    # first get class_list.txt file form school folder
    get_class_list_file = open('schools/heysushil/class_list.txt', 'r')
    get_classes_in_list = get_class_list_file.readlines()
    # use for loop to show number and school name
    print('\nHello Admin,\nYe hamari existing classes list hai.\nJis class me enter karna hai us number ko enter kariye: \n')
    # blank list to get all class names
    class_list_for_options = []
    # for i, name in enumerate(get_classes_in_list, start=1):
    i = 1
    for name in get_classes_in_list:
        # name.strip() method use to remove starting or ending space of special char
        
        # use condtion to handle blank data
        if bool(name.strip()) == True:
            print('{} {} Class'.format(i, name.strip()))
            i += 1 # for showing continus number on list
            class_list_for_options.append(name.strip())
    get_class_list_file.close()

    # get class name by admin
    # print(class_list_for_options)
    # exit()

    # Here need to handel error when admin tring to enter non numeric number of outof range number
    # then create function for choose available class on existing school

    # use try except to handle probel
    try:
        option = int(input('\nEnter class number: '))
    except ValueError:
        print('\nAap ne number ki jagah kuch aur input kiya hai. Kripya sahi input ke sath dubara try kare?')
        # call choices function
        class_choices(school_name)
    except NameError:
        print('\nAap ne alphabet input kiya hai jo ki galat hai. Sahi input ke sath dubara try kariye?')
        # call choices function
        class_choices(school_name)
    except:
        print('\nInput me koi problem aai hai. Kripya sahi input ke sath dubara try kare?')
        # call choices function
        class_choices(school_name)
    else:
        # print('\nAdmin option: ', school_list_for_options[option-1])
        # call chooce class options function
        class_name = class_list_for_options[option-1]
        
        # Ab class ke andar jo options show karne hai unka function
        student_options_in_class(school_name, class_name)



# Ye ek class ke andar hone wale activites ka function hai
def student_options_in_class(school_name, class_name):
    message = '''
    ---------------------------------
                {0} Class
    ---------------------------------
    1. Register New Student
    2. Check Student Details
    3. Update Student Detail
    4. Delete Student
    5. Exit
    ---------------------------------
    Only enter numbers:         
    '''.format(class_name)
    try:
        option = int(input(message))
    except ValueError:
        print('\nAap ne number ki jagah kuch aur input kiya hai. Kripya sahi input ke sath dubara try kare?')
        # call choices function
        # school_choices()
    except NameError:
        print('\nAap ne alphabet input kiya hai jo ki galat hai. Sahi input ke sath dubara try kariye?')
        # call choices function
        # school_choices()
    except:
        print('\nInput me koi problem aai hai. Kripya sahi input ke sath dubara try kare?')
        # call choices function
        # school_choices()
    else:
        if option == 1:
            student.register_new_student(school_name, class_name)
        elif option == 2:
            student.check_student_detail(school_name, class_name)
        elif option == 3:
            student.update_student_detail(school_name, class_name)
        elif option == 4:
            student.delete_student(school_name, class_name)
        elif option == 5:
            print('\nAdmin aap safalta purvak exit kar chuke hain.')
        else:
            print('\nAap ne galt input diya hai. Dubara sahi input choice ke sath try kare.')
            # call choices function
            # school_choices()

# Fucntion class choice ke liye
def class_choices(school_name):
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
            choose_class(school_name)
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
        class_choices(school_name)

# Choose school fucntion: Yaha se existing school folder ke andar enter honge.
def choose_school():
    # first get school_list.txt file
    import os
    # os.path
    # working_directory = os.getcwd()
    get_school_list_file = open('school_list.txt', 'r')
    get_schools_in_list = get_school_list_file.readlines()
    # use for loop to show number and school name
    print('\nHello Admin,\nYe hamari existing school list hai.\nJis school me enter karna hai us number ko enter kariye: \n')
    # blank list to get all school names
    school_list_for_options = []
    for i, name in enumerate(get_schools_in_list, start=1):
        # name.strip() method use to remove starting or ending space of special char
        print('{} {}'.format(i, name.strip()))
        school_list_for_options.append(name.strip())
    get_school_list_file.close()

    # get school name by admin
    # print(school_list_for_options)

    # Here need to handel error when admin tring to enter non numeric number of outof range number
    # then create function for choose available class on existing school

    # use try except to handle probel
    try:
        option = int(input('\nEnter school number: '))
    except ValueError:
        print('\nAap ne number ki jagah kuch aur input kiya hai. Kripya sahi input ke sath dubara try kare?')
        # call choices function
        school_choices()
    except NameError:
        print('\nAap ne alphabet input kiya hai jo ki galat hai. Sahi input ke sath dubara try kariye?')
        # call choices function
        school_choices()
    except:
        print('\nInput me koi problem aai hai. Kripya sahi input ke sath dubara try kare?')
        # call choices function
        school_choices()
    else:
        # print('\nAdmin option: ', school_list_for_options[option-1])
        # call chooce class options function
        school_name = school_list_for_options[option-1]
        class_choices(school_name)


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
    # call choices function
    school_choices()
except NameError:
    print('\nAap ne alphabet input kiya hai jo ki galat hai. Sahi input ke sath dubara try kariye?')
    # call choices function
    school_choices()
except:
    print('\nInput me koi problem aai hai. Kripya sahi input ke sath dubara try kare?')
    # call choices function
    school_choices()
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
        # call choices function
        school_choices()
