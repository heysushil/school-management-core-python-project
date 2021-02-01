import json

# roll number check karne ke liye
def check_roll_number(school_name, class_name, roll_number):
    # student_details name ki file ko read mode me open kiya, taki is file me se roll number get kiya ja sake.
        get_studnet_details = open('schools/'+school_name+'/'+class_name+'/student_details.txt', 'r')
        get_roll_number = get_studnet_details.readlines()
        # get_individual_rn = []
        # str to dictinary conversion ke liye json ka use karenge.
        for r in get_roll_number:
            # print('type: ', type(json.loads(r)))
            e_rn = json.loads(r) # e_rn = existing roll number
            # print(e_rn)
            existing_rn = e_rn['roll_number']
            # check roll number
            if roll_number == existing_rn:
                print('\nThis roll number', roll_number, 'is already exists. Pleas try a new.')
                # return get_roll_number
                print('\nNaye student ka registration uniqe roll number ke sath kare:\n')
                register_new_student(school_name, class_name)

# for registering new stuent
def register_new_student(school_name, class_name):
    try:
        roll_number = int(input('\nEnter your roll number: '))
        check_roll_number(school_name, class_name, roll_number)
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

        print('\nNew student registration safalta purvas ho chuka hai.')

def check_student_detail(class_name):
    print('\ncheck_student_detail(class_name): ', class_name)

def update_student_detail(class_name):
    print('\nupdate_student_detail(class_name): ', class_name)

def delete_student(class_name):
    print('\ndelete_student(class_name): ', class_name)