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
            check_student_detail(school_name, class_name)
        elif option == 3:
            update_student_detail(school_name, class_name)
        elif option == 4:
            delete_student(school_name, class_name)
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

def get_student_data_by_rollnumber(school_name, class_name, roll_number):
    # student_details name ki file ko read mode me open kiya, taki is file me se roll number get kiya ja sake.
        get_studnet_details = open('schools/'+school_name+'/'+class_name+'/student_details.txt', 'r')
        get_roll_number = get_studnet_details.readlines()

        # print('\nCheck get all roll numebr: ', get_roll_number)
        # exit()
        # loop me individula roll number ko get karna hai
        get_individual_rn = []
        for r in get_roll_number:
            # print('Type: ', type(json.loads(r)))
            all_rn_as_dict = json.loads(r)
            get_single_roll_number = all_rn_as_dict['roll_number']
            # print('\nRoll number: ', get_single_roll_number)

            # ab existing roll number me se new roll number ko check karn ahai using condition
            if roll_number == get_single_roll_number:
                message = '\nIs student ki sari details: => \n\n'
                # register_new_student(school_name, class_name)
                return all_rn_as_dict

        # return print('\nTHis is studnets roll number: ', roll_number)        

# existing studnet ki detail ko dekhne ke liye hame kya chaiye
# school name, class name, roll number
def check_student_detail(school_name, class_name):
    roll_number = int(input('\nEnter student roll number: '))
    result = get_student_data_by_rollnumber(school_name, class_name, roll_number)
    print('''
    ----------------------------------
            Student Details
    ----------------------------------
    Roll Number  : {}         
    Student Name : {}      
    Class Name   : {}    
    Father's Name: {}       
    Mother's Name: {}       
    Mobile Number: {}       
    Address      : {} 
    ----------------------------------
    '''.format(result['roll_number'], result['name'], result['my_class_name'], result['father_name'], result['mother_name'], result['mobile'], result['address']))

    return result

    # student name: name
    # father name: f name

# student update data ke liye option ka function
def choose_student_update_options(school_name, class_name, student_data):
    message = '''
    ---------------------------------
                {} student's detail
    ---------------------------------       
    1. Student Name  : {}                 
    2. Father's Name : {}           
    3. Mother's Name : {}           
    4. Mobile Number : {}           
    5. Address       : {}     
    -------------------------
    Only enter numbers:         
    '''.format(student_data['name'],student_data['name'],student_data['father_name'], student_data['mother_name'], student_data['mobile'], student_data['address'])
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
            updated_student_name = input('\n Enter students right name: ')
            # open file with write mode.
            get_studnet_details = open('schools/'+school_name+'/'+class_name+'/student_details.txt', 'r')
            get_roll_number = get_studnet_details.readlines()
            get_studnet_details.close()
            for r in get_roll_number:
                # print('Type: ', type(json.loads(r)))
                all_rn_as_dict = json.loads(r)
                get_single_roll_number = all_rn_as_dict['roll_number']
                # print('\nRoll number: ', get_single_roll_number)

                # ab existing roll number me se new roll number ko check karn ahai using condition
                if student_data['roll_number'] == get_single_roll_number:
                    message = '\nStudent mil gaya hai jiski detail ko update karna hai: Exisiting name: => ', student_data['name'] , 'Update kare wala name:', updated_student_name
                    print('\n', message)
                    # register_new_student(school_name, class_name)
                    # return all_rn_as_dict

                    # exsiting dictionary ke kisi ek value ko update karne ke liye hun fileinput library ka use karenge.
                    import fileinput
                    filename = 'schools/'+school_name+'/'+class_name+'/student_details.txt'
                    with fileinput.FileInput(filename, inplace=True, backup = '.bak') as f:
                        # print('\nF ke andar ka data: ', f)
                        # exit()
                        for line in f:
                            # print('\ntype of student_data: ', type(student_data))
                            if(json.dumps(student_data)+'\n' == line):
                                new_data = json.dumps({"roll_number": student_data['roll_number'], "name": updated_student_name, "my_class_name": student_data['my_class_name'], "father_name": student_data['father_name'], "mother_name": student_data['mother_name'], "address": student_data['address'], "mobile": student_data['mobile']})
                                print(new_data)
                            else:
                                print(line, end='')

                        print('\nStudent name successfully udpate ho chuka hai.')
                        student_options_in_class(school_name, class_name)

        elif option == 2:            
            updated_father_name = input('\n Enter students father name: ')            
            import fileinput
            filename = 'schools/'+school_name+'/'+class_name+'/student_details.txt'
            with fileinput.FileInput(filename, inplace=True, backup = '.bak') as f:
                # print('\nF ke andar ka data: ', f)
                # exit()
                for line in f:
                    # print('\ntype of student_data: ', type(student_data))
                    if(json.dumps(student_data)+'\n' == line):
                        new_data = json.dumps({"roll_number": student_data['roll_number'], "name": student_data['name'], "my_class_name": student_data['my_class_name'], "father_name": updated_father_name, "mother_name": student_data['mother_name'], "address": student_data['address'], "mobile": student_data['mobile']})
                        print(new_data)
                    else:
                        print(line, end='')

                print('\nStudent father name successfully udpate ho chuka hai.')
                student_options_in_class(school_name, class_name)
        elif option == 3:
            update_data = input('\n Enter students mother name: ')            
            import fileinput
            filename = 'schools/'+school_name+'/'+class_name+'/student_details.txt'
            with fileinput.FileInput(filename, inplace=True, backup = '.bak') as f:
                for line in f:                    
                    if(json.dumps(student_data)+'\n' == line):
                        new_data = json.dumps({"roll_number": student_data['roll_number'], "name": student_data['name'], "my_class_name": student_data['my_class_name'], "father_name": student_data['father_name'], "mother_name": update_data, "address": student_data['address'], "mobile": student_data['mobile']})
                        print(new_data)
                    else:
                        print(line, end='')
                print('\nStudent mother name successfully udpate ho chuka hai.')
                student_options_in_class(school_name, class_name)
        elif option == 4:
            update_data = input('\n Enter students right mobile number: ')            
            import fileinput
            filename = 'schools/'+school_name+'/'+class_name+'/student_details.txt'
            with fileinput.FileInput(filename, inplace=True, backup = '.bak') as f:
                for line in f:                    
                    if(json.dumps(student_data)+'\n' == line):
                        new_data = json.dumps({"roll_number": student_data['roll_number'], "name": student_data['name'], "my_class_name": student_data['my_class_name'], "father_name": student_data['father_name'], "mother_name": student_data['mother_name'], "address": student_data['address'], "mobile": update_data})
                        print(new_data)
                    else:
                        print(line, end='')
                print('\nStudent mobile successfully udpate ho chuka hai.')
                student_options_in_class(school_name, class_name)
        elif option == 5:
            update_data = input('\n Enter students right address: ')            
            import fileinput
            filename = 'schools/'+school_name+'/'+class_name+'/student_details.txt'
            with fileinput.FileInput(filename, inplace=True, backup = '.bak') as f:
                for line in f:                    
                    if(json.dumps(student_data)+'\n' == line):
                        new_data = json.dumps({"roll_number": student_data['roll_number'], "name": student_data['name'], "my_class_name": student_data['my_class_name'], "father_name": student_data['father_name'], "mother_name": student_data['mother_name'], "address": update_data, "mobile": student_data['mobile']})
                        print(new_data)
                    else:
                        print(line, end='')
                print('\nStudent address successfully udpate ho chuka hai.')
                student_options_in_class(school_name, class_name)
        else:
            print('\n sahi option nahi chuna')
            student_options_in_class(school_name, class_name)

# yaha par bhi ham ko sabse pahle school name aur class name cahiye hai aur sath me roll number bhi cahiye hai.
def update_student_detail(school_name, class_name):
    # print('\nSchool name: ', school_name)
    # print('\nClass name: ', class_name)
    get_student_data = check_student_detail(school_name, class_name)
    print('\nKya get sutdent data mila: \n\n', get_student_data)

    # option create karna hai ki kaunsa detail update karna hai uske liye.
    choose_student_update_options(school_name, class_name, get_student_data)

def delete_student(school_name, class_name):
    student_data = check_student_detail(school_name, class_name)
    print('\nKya get sutdent data mila: \n\n', student_data)
    
    # update_data = input('\n Enter students right address: ')
    import fileinput
    filename = 'schools/'+school_name+'/'+class_name+'/student_details.txt'
    with fileinput.FileInput(filename, inplace=True, backup = '.bak') as f:
        for line in f:
            if(json.dumps(student_data)+'\n' == line):
                print(end='')
            else:
                print(line, end='')
        print('\nStudent data successfully delete ho chuka hai.')
        student_options_in_class(school_name, class_name)

# @heysushil