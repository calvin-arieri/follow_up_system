from students import Student, Parent , Student_results, Student_behaviour
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from principal import Principal
from otherUsers import Other_user
from tabulate import tabulate

def create_new_student():
    # Promts users to enter required information
    print("Please add your details:")
    st_id = None
    st_fn = input("First Name: ")
    st_Sn = input("Second name: ")  
    st_uc = input("Surname:  ")
    st_Sc = input("School code shared by principal: ")
    # Adds new student to the database
    new_student = Student(student_id=st_id, student_first_name = st_fn, student_second_name = st_Sn, student_surname = st_uc, school_code = st_Sc)
    session.add(new_student)
    session.commit()

    # Finds new student to assign them a new unique key
    student_code = session.query(Student).all()
    for student in student_code:
        if student.student_first_name == st_fn and student.student_second_name == st_Sn and student.student_surname == st_uc and student.school_code== st_Sc:
            # add the student unique code.
            
            add_unique_code = session.query(Student).filter(Student.student_id == student.student_id).first()                    
            # Gives criteria of assigning the new student indentification code

            new_student_code =f"s{student.student_first_name[0]}{student.student_first_name[2]}{student.student_id}{student.student_surname[-1]}{st_Sc}"
            add_unique_code.unique_code = new_student_code
            session.commit()

            # message to confirm registration
            print(f"Thank you for registering with us you log in code is {new_student_code}")
# add new parent
def create_new_parent():
    print("Welcome to our system we are happy to work with you to make you son works hard and is disciplined in school")
    # gets the required input to  create a parent
    the_one = input("Your child code: ")
    print("Please enter the required details below")
    pa_id= None
    pa_name = input("Your full names: " )
    pa_ph = input("Your phone number: ")
    # enter values to be fed to the table
    new_parent = Parent(parent_id = pa_id, parent_name = pa_name, parent_phone=pa_ph, student_code = the_one)
    # pushes ths values to a database
    session.add(new_parent)
    session.commit()
    
    # generates the loging code of the new parent
    give_code = session.query(Parent).filter(Parent.parent_name == pa_name, Parent.parent_phone ==pa_ph).first()
    the_code = f"p{give_code.parent_id*21}s{give_code.parent_name[0:2]}"
    give_code.parent_log_in = the_code
    session.commit()
    # output the loging/user  code for the parent.
    print(f"Welcome {pa_name} your log/user in code is {the_code}")

# add new principal
def create_new_principal():
    print("Thank you for choosing our system.Provide the following info to add you to the system.")

    # getting details of the new principal
    p_id = None
    p_reg =int(input("T.S.C number: "))
    p_s = input("School code: ")
    p_n = input("Your full name: ")
    p_n_p = int(input("Your phone number: "))
    # creating the new principal  

    new_principal = Principal(principal_id=p_id ,principal_reg = p_reg,  principal_school = p_s, principal_name = p_n, principal_phone_number = p_n_p)
    # Adding the principal to the database

    session.add(new_principal)
    session.commit()

    # generating the principal user/log  code
    print(f"Welcome {p_n} your usercode is a{p_reg}") 

# add new company
def create_new_company():
    print("Thank you for choosing our system to get a person information before hiring them.")
    print("Before you continue please register with us")
    u_id = None
    u_n = input("User Name: ")
    u_p = input("password: ")
    c_n = input("Company Name: ")

    new_company = Other_user(user_id = u_id, user_name = u_n, user_password = u_p, company_name = c_n) 
    session.add(new_company)
    session.commit()
    print(f"Welcome {c_n} we are happy to work with your user code is c{u_p}")
    
# add new result
def add_new_result(unique_cod):
    print("Happy to know the exams are done. Please enter the results below to start the computation")

    # get the results details
    r_id = None
    r_p = int(input("Perfomance in terms of points: ")) 

    # gets the average to find the percentage perfomance
    the_avg = (r_p / 84)*100   

    # creates new result instance
    new_result = Student_results(result_id = r_id, result_points = r_p, student_unique_code = unique_cod, student_perfomance= the_avg)
    session.add(new_result)
    session.commit()
    print(f"The results have been added successfully. The student has {the_avg}%")


# add misbehaviour case for the principal only
def add_misbehave(school_id, uniqu_cod):
    # Gets misbehaviour
    print('Please fill the detail below')
    m_id = None
    s_m_b = input('The mistake: ')
    new_misbehave = Student_behaviour(misbehaviour_id = m_id, student_unique_code = uniqu_cod, student_misbehave = s_m_b, school_code = school_id )
    session.add(new_misbehave)
    session.commit()
    print('You have successfully added the misbehaviour of the student')

# printsa all the students in the school this is only for the principal there
def get_students_school(school_cod):
    print("Here are the number of students in your school")
    student_numbers = 0
    the_students = session.query(Student).filter(Student.school_code == school_cod).all()
    table = []    
    for student in the_students:
        student_numbers += 1
        data = [student_numbers , student.student_first_name , student.student_second_name, student.student_surname , student.unique_code] 
        table.append(data)
    print(tabulate(table, headers=['Number',"First Name", 'Second name', 'Surname', 'Unique code'])) 

def get_student_results():
    print('Here are the students results')

# Prints the behavior of student accoreding to a certain school only for the principals
def get_students_behaviour(school_id):

    the_mis = session.query(Student_behaviour).filter(Student_behaviour.school_code == school_id).all()
    table = []
    for the_mi in the_mis:
        student_name = session.query(Student).filter(Student.unique_code == the_mi.student_unique_code).first()
        data = [the_mi.misbehaviour_id,f'{student_name.student_first_name} {student_name.student_second_name}', the_mi.student_misbehave]
        table.append(data)
    print(tabulate(table, headers=['misbehaviour id', 'Student name', 'Mistake']))    

# fetching the student indiscipline cases of the parents child
def parent_get_student_behaviour(unque_cod):
    the_children = session.query(Student_behaviour).filter(Student_behaviour.student_unique_code == unque_cod).all()
    the_mistakes = []
    for mis in the_children:
        the_mistakes.append(mis.student_misbehave)
    print(the_mistakes)   

# fetching the students result
def parent_get_student_result(unique_cod):
    the_results = session.query(Student_results).filter(Student_results.student_unique_code == unique_cod).all()
    for result in the_results:
        print(result.result_points, result.student_perfomance)

def student_rating(unique_cod):
    the_results = session.query(Student_results).filter(Student_results.student_unique_code == unique_cod).all()
    result_sum = 0
    number_of_exams = 0
    for result in  the_results:
         number_of_exams += 1
         result_sum = result_sum + result.student_perfomance
    the_average = result_sum / number_of_exams
    the_children = session.query(Student_behaviour).filter(Student_behaviour.student_unique_code == unique_cod).count()
    if the_children < 2:
        rate = 100
    elif the_children > 2 and the_children < 5:
        rate = 75
    elif the_children > 5 and the_children > 7:
        rate  = 50
    elif the_children> 9 and the_children < 11:
        rate = 25 
    else:
        rate = 0

    the_rating_of = (the_average + rate) / 2

    if the_rating_of < 101 and the_rating_of >= 75:
        msg = "Good and well behaved student"
    elif the_rating_of < 75 and the_rating_of >= 50:
        msg = "The student is an average student in terms of behaviour and results"
    elif the_rating_of < 50  and the_rating_of >= 25:
        msg = "Good but requires supervision "
    else:
        msg = "Cannot recommend him"  
    print(tabulate( [['Academic perfomance in %', 'Discipline percentage', 'Average rating', 'What to say about rating'],[the_average, rate,the_rating_of, msg ]], headers='firstrow'))      
                      

# creating the session
engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()



# the main menu for the users.
def main(user_id):
    find_category = user_id[0]
    if find_category == "s":
        the_details = session.query(Student).filter(Student.unique_code == user_id).first()
        print(f"Welcome back {the_details.student_second_name} {the_details.student_surname},")
        print("What details do tou want to see today")
        option_for = ('Results', 'Behaviour', 'Rating', 'quit')
        the = 0
        for option in option_for:
            the += 1
            print(f'{the}. {option}')
        one_option = input("choose one: ")
        if one_option == '1':
            parent_get_student_result(user_id)
        elif one_option == '2':
            parent_get_student_behaviour(user_id) 
        elif one_option == '3':
            student_rating(user_id)
        elif one_option  == '4':
            print(f'You have sucssefully exited the application hope to see you {the_details.student_first_name}')  
        else:
            print('Invalid input')

    elif find_category == 'p':
        the_details = session.query(Parent).filter(Parent.parent_log_in == user_id).first()
        print(f'welcome back {the_details.parent_name}')
        option_for = ('Results', 'Behaviour', 'Rating', 'quit')
        the = 0
        for option in option_for:
            the += 1
            print(f'{the}. {option}')
        the_option = input('choose one option: ') 
        if the_option == "1":
            parent_get_student_result(the_details.student_code)
        elif the_option == '2':
            parent_get_student_behaviour(the_details.student_code)
        elif the_option == '3':
            student_rating(the_details.student_code)
        elif the_option == '3':
            print('You have successfuly exited the program')
        else:
            print('invalid output')  
    elif find_category == 'c':
        password = user_id[1:6]
        print(password)
        the_company = session.query(Other_user).filter(Other_user.user_password == password).first()
        print(f'Welcome back {the_company.company_name}')
        the_code = input("The student code: ")
        student_rating(the_code)

    elif find_category == 'a':
        the_search_code = user_id[1:6]
        the_int = int(the_search_code)
        get_principal = session.query(Principal).filter(Principal.principal_reg == the_int).first()
        print(f"Welcome back {get_principal.principal_name},")
        print('Do you want to:')
        print('1. Add details')
        print('2. View details')
        print('3.Delete student')
        print('4. Quit')
        the_choice = input('Choose one: ')
        if the_choice == '1':
            print('Choose one option: ')
            options = ('Results', 'Behaviour')
            number_of = 0
            for option in options:
                number_of += 1
                print(f"{number_of}. {option}")
            receive_option = input("Choose one from the above")
            if receive_option == "1":
                student_unique_number = input("Please key in student unique number: ")
                find_out = session.query(Student).filter(Student.unique_code == student_unique_number).first()
                if find_out.school_code == get_principal.principal_school:
                    add_new_result(student_unique_number)
                else:
                    print("You are not allowed to change any detail of the student.")  

            elif receive_option == "2":
                student_unique_number = input("Please key in student unique number: ")
                find_out = session.query(Student).filter(Student.unique_code == student_unique_number).first()
                if find_out.school_code == get_principal.principal_school:
                    add_misbehave(get_principal.principal_school ,student_unique_number)
                else:
                    print("You are not allowed to change any detail of the student.")                  
            else:
                print("Invalid input")
        elif the_choice == "2":
            print('Welcome to the view details section')
            options = ("Students", 'Misbehaviours', 'student rating', 'student perfomance', 'student parent')
            num = 0
            for option in options:
                num += 1
                print(f'{num}. {option}')
            the_opt = input('Choode one: ')
            if the_opt   == '1':
                get_students_school(get_principal.principal_school) 
            elif the_opt == '2':
                get_students_behaviour(get_principal.principal_school) 
            elif the_opt == '3':
                print('To know rating')
                the_code = input("The student code: ")
                student_rating(the_code)
            elif the_opt == '4':
                    the_students = session.query(Student).filter(Student.school_code == get_principal.principal_school).all()
                    table = []
                    for student in the_students:
                        the_result = session.query(Student_results).filter(Student_results.student_unique_code == student.unique_code).all()
                        for result in the_result:
                            data = [result.result_id ,f'{student.student_first_name, student.student_second_name, student.student_surname}', result.student_perfomance]
                            table.append(data)
                    print(tabulate(table, headers=['Exam id', 'Student full Names', 'Student perfomance in %'])) 
                           
            elif the_opt == '5':
                the_code = input('Please add the student code: ')
                the_parent = session.query(Parent).filter(Parent.student_code == the_code).first()
                print(tabulate([['Id', 'Name', 'Phone number', 'User code'],[the_parent.parent_id,the_parent.parent_name,the_parent.parent_phone,the_parent.parent_log_in]],headers='firstrow'))
        elif the_choice == '3':
            print("Input student user code to be deleted")
            user_code = input('User code: ')
            find_out = session.query(Student).filter(Student.unique_code == user_code).first()
            if find_out.school_code == get_principal.principal_school:
                print(f'You have succesfully deleted {find_out.student_first_name} {find_out.student_second_name} {find_out.student_surname}')
                session.delete(find_out)
                session.commit()
            else:
                print("You cannot delete the student since you are not the school principal")  
        elif the_choice == '4':
            print('You have successfully exited the programme')
        else:
            print('Invalid output')                
            # start from here tommorrow


if __name__ == "__main__":
    # welcomes you to the system 
    print("Welcome to school management system")
    print("Are you an existing member?")
    print("1. Yes")
    print("2. No")
    # Receive options
    get_choice = input("Choose one: ")
    # log if in the system
    if get_choice == "1": 
        user_id = input("Please enter your user number: ")
        main(user_id)
        # register if not in the system
    elif get_choice == "2":
        print("Please register with us to use this system.")  
        print("Do you want to regster as:") 
        # Gives list of people to be registered
        list_of_choices = ("Student", "Parent", "Principal", "Company")
        #  Returns the options availablen
        num = 0
        for choice in list_of_choices:
            num += 1
            print(f"{num}. {choice}")
            # prompts user to chose their choice
        the_chosen = input("Please choose one: ") 
        # The users choice
        if the_chosen == "1":
             create_new_student()                    
                    # Application of a new parent.
        elif the_chosen == "2":
            # must have a student code to register as ne parent
            print("Once you child has identification code you can now proceed to this step.")
            print("Does your child have an Identification code?") 
            print("1. Yes")
            print("2. No")
            # If lacks the student code
            present_code = input("Choose one option: ")
            if present_code == "2":
                # Output messages
                print("Apply for the code. And one has applied for it please wait for response from the school so that you can register")
                print("Thank you for showing interest in our system.")
                # if has student code
            if present_code == "1":
                # calls the creating new parent function
                create_new_parent()
        elif the_chosen == "3":
            # calls the new principal function
            create_new_principal()
        elif the_chosen == "4":
            # calls the new company function
            create_new_company()        

             

