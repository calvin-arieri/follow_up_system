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

def create_new_parent():
    print("Welcome to our system we are happy to work with you to make you son works hard and is disciplined in school")
    the_one = input("Your child code: ")
    print("Please enter the required details below")
    pa_id= None
    pa_name = input("Your full names: " )
    pa_ph = input("Your phone number: ")
    new_parent = Parent(parent_id = pa_id, parent_name = pa_name, parent_phone=pa_ph, student_code = the_one)
    session.add(new_parent)
    session.commit()
    give_code = session.query(Parent).filter(Parent.parent_name == pa_name, Parent.parent_phone ==pa_ph).first()
    the_code = f"p{give_code.parent_id*21}s{give_code.parent_name[0:2]}"
    give_code.parent_log_in = the_code
    session.commit()
    print(f"Welcome {pa_name} your log/user in code is {the_code}")

def create_new_principal():
    print("Thank you for choosing our system.Provide the following info to add you to the system.")
    p_id = None
    p_reg =int(input("T.S.C number: "))
    p_s = input("School code: ")
    p_n = input("Your full name: ")
    p_n_p = int(input("Your phone number: "))

    new_principal = Principal(principal_id=p_id ,principal_reg = p_reg,  principal_school = p_s, principal_name = p_n, principal_phone_number = p_n_p)

    session.add(new_principal)
    session.commit()
    print(f"Welcome {p_n} your usercode is a{p_reg}") 

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

def add_new_result():
    print("Happy to know the exams are done. Please enter the results below to start the computation")
    r_id = None
    r_p = int(input("Perfomance in terms of points: ")) 
    s_u_c = ('Student unique code: ')
    the_avg = r_p // 84
    s_P = the_avg * 100
    new_result = Student_results(result_id = r_id, result_points = r_p, student_unique_code = s_u_c, student_perfomance= s_P)
    session.add(new_result)
    session.commit()
    print(f"The results have been added successfully. The student has {s_P}%")

def add_misbehave(school_id):
    print('Add information below to add the misbehave')
    m_id = None
    s_u_c = input("Unique code: ")
    s_m_b = input('The mistake: ')
    new_misbehave = Student_behaviour(misbehaviour_id = m_id, student_unique_code = s_u_c, student_misbehave = s_m_b, school_code = school_id )
    session.add(new_misbehave)
    session.commit()
    print('You have successfully added the misbehaviour of the student')

def get_students_school(school_cod):
    print("Here are the number of students in your school")
    student_numbers = 0
    the_students = session.query(Student).filter(Student.school_code == school_cod).all()
    table = []    
    for student in the_students:
        student_numbers += 1
        data = [student.student_first_name , student.student_second_name, student.student_surname , student.unique_code] 
        table.append(data)
    print(tabulate(table, headers=["First Name", 'Second name', 'Surname', 'Unique code'])) 

def get_student_results():
    print('Here are the students results')

def get_students_behaviour(school_id):
    the_mis = session.query(Student_behaviour).filter(Student_behaviour.school_code == school_id).all()
    for the_mi in the_mis:
        print(the_mi.misbehaviour_id, the_mi.student_unique_code, the_mi.student_misbehave)

def parent_get_student_behaviour(unque_cod):
    the_children = session.query(Student_behaviour).filter(Student_behaviour.student_unique_code == unque_cod).all()
    for mis in the_children:
        print(mis.student_misbehave)

def parent_get_student_result(unique_cod):
    the_results = session.query(Student_results).filter(Student_results.student_unique_code == unique_cod)
    for result in the_results:
        print(result.result_points, result.student_perfomance)

engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()

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
            print('work on it')
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
            print('still working on this')
        elif the_option == '3':
            print('You have successfuly exited the program')
        else:
            print('invalid output')  
    elif find_category == 'c':
        pass

    elif find_category == 'a':
        the_search_code = user_id[1:6]
        the_int = int(the_search_code)
        get_principal = session.query(Principal).filter(Principal.principal_reg == the_int).first()
        print(f"Welcome back {get_principal.principal_name},")
        print('Do you want to:')
        print('1. Add details')
        print('2. View details')
        print('3. Quit')
        the_choice = input('Choose one: ')
        if the_choice == '1':
            print('Choose one option: ')
            options = ('Results', 'Behaviour')
            # start from here tommorrow
            

if __name__ == "__main__": 
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
        list_of_choices = ["Student", "Parent", "Principal", "Company"]

        #  Returns the options available
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
                create_new_parent()

        elif the_chosen == "3":
            create_new_principal()

        elif the_chosen == "4":
            create_new_company()        

             

