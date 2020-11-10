# for registering new stuent
def register_new_student(school_name, class_name):
    try:
        roll_number = int(input('\nEnter your roll number: '))
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
        open('schools/'+school_name+'/'+class_name+'/student_details.txt', 'a')

def check_student_detail(class_name):
    print('\ncheck_student_detail(class_name): ', class_name)

def update_student_detail(class_name):
    print('\nupdate_student_detail(class_name): ', class_name)

def delete_student(class_name):
    print('\ndelete_student(class_name): ', class_name)