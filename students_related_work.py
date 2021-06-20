import json
# import main

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
            register_new_student(school_name, class_name)
        elif option == 2:
            check_student_detail(class_name)
        elif option == 3:
            update_student_detail(class_name)
        elif option == 4:
            delete_student(class_name)
        elif option == 5:
            print('\nAdmin aap safalta purvak exit kar chuke hain.')
        else:
            print('\nAap ne galt input diya hai. Dubara sahi input choice ke sath try kare.')
            # call choices function
            # school_choices()

# roll number check karne ke liye
def check_roll_number(school_name, class_name, roll_number):
    # student_details name ki file ko read mode me open kiya, taki is file me se roll number get kiya ja sake.
        get_studnet_details = open('schools/'+school_name+'/'+class_name+'/student_details.txt', 'r')
        get_roll_number = get_studnet_details.readlines()

        # loop me individula roll number ko get karna hai
        get_individual_rn = []
        for r in get_roll_number:
            # print('Type: ', type(json.loads(r)))
            all_rn_as_dict = json.loads(r)
            get_single_roll_number = all_rn_as_dict['roll_number']
            # print('\nRoll number: ', get_single_roll_number)

            # ab existing roll number me se new roll number ko check karn ahai using condition
            if roll_number == get_single_roll_number:
                message = '\nYe roll number => ', roll_number ,' <= pahle se hai. New roll number try karen.'
                # register_new_student(school_name, class_name)
                return message

        # return print('\nTHis is studnets roll number: ', roll_number)        

# for registering new stuent
def register_new_student(school_name, class_name):
    try:        
        # roll number ko chekc karne ke liye sab se pahle entered roll number ko function ko pass karna hai.
        roll_number = int(input('\nEnter student roll number: '))

        recive_message = check_roll_number(school_name, class_name, roll_number)
        
        # print('\ncheck recive message variable: ', recive_message)

        if recive_message:
            print(recive_message)
            roll_number = int(input('\nEnter student roll number: '))

        # print(recive_result)
        # exit()
        
        name = input('\nEnter stduent name: ')
        my_class_name = class_name
        father_name = input('\nEnter student\'s father name: ')
        mother_name = input('\nEnter student\'s mother name: ')
        address = input('\nEnter student\'s address: ')
        mobile = int(input('\nEnter student\'s mobile number: '))
    except:
        print('\nAapne input me galti ki hai dubara try kare.')
    else:
        student_data = {
            'roll_number' : roll_number,
            'name' : name,
            'my_class_name' : my_class_name,
            'father_name' : father_name,
            'mother_name' : mother_name,
            'address' : address,
            'mobile' : mobile,            
        }

        # print('\nComplete student data: ', student_data)

        # create a new file and append student data
        myfile = open('schools/'+school_name+'/'+class_name+'/student_details.txt', 'a')

        # dictionary data ko string me convert karne ke liye hame json ka use karn hai.
        
        # add student_data on text file
        # print('\nCheck student data typs: ', type(json.dumps(student_data)))
        myfile.write('\n'+json.dumps(student_data))
        myfile.close()

        print('\nNew student registration safalta purvas ho chuka hai.\n\n')
        student_options_in_class(school_name, class_name)

def check_student_detail(class_name):
    roll_number = int(input('\nEnter student roll number: '))

def update_student_detail(class_name):
    print('\nupdate_student_detail(class_name): ', class_name)

def delete_student(class_name):
    print('\ndelete_student(class_name): ', class_name)