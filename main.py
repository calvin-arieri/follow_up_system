from students import Student
from sqlalchemy import  String, Column, Integer , create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from principal import Principal
from otherUsers import Other_user

engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()
def main(session, user_id):
    # print("Welcome to person info management.Choose one option")
    # the_options = ["Principal", "Company", "Parent", "Student", "Quit"]
    # num = 0
    # for option in the_options:
    #     num += 1
    #     print(f"{num}. {option}")
    # chosen_option = input("Choose one: ")
    # if option == "1":
    #     print("welcome to the principal portal.") 
    print(user_id)


if __name__ == "__main__": 
    print("Welcome to school management system")
    print("Are you an existing member?")
    print("1. Yes")
    print("2. No")

    # Receive options
    get_choice = input("Choose one: ")

    # log if in the system
    if get_choice == "1":
        user_id = input("Please ented your indentification number: ")
        main(session, user_id)

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

                    # message to confirm registration
                    print(f"Thank you for registering with us you log in code is {new_student_code}")
                    
                    # Application of a new parent.
        elif the_chosen == "2":

            # must have a student code to register as ne parent
            print("Once you child has identification code you can now proceed to this step.")
            print("Does your child have an Identification code?") 
            print("1. Yes")
            print("2. No")

            # If lacks the student code
            present_code = input("Choose 1")
            if present_code == "2":

                # Output messages
                print("Apply for the code. And one has applied for it please wait for response from the school so that you can register")
                print("Thank you for showing interest in our system.")

                # if has student code
            if present_code == "1":
                print("Welcome to our system we are happy to work with you to make you son works hard and is discipline in school")
                the_one = input("Your child code: ")
                # will continue once figured how to udate record

        elif the_chosen == "3":
            print("Thank you for choosing our system.Provide the following info to add you to the system.")
            p_id = None
            p_reg =int(input("T.S.C number: "))
            p_s = input("School code: ")
            p_n = input("Your full name: ")
            p_n_p = int(input("Your phone number: "))

            new_principal = Principal(principal_id=p_id ,principal_reg = p_reg,  principal_school = p_s, principal_name = p_n, principal_phone_number = p_n_p)

            session.add(new_principal)
            session.commit()
            # will add log in code here

        elif the_chosen == "4":
            print("Thank you for choosing our system to get a person information before hiring them.")
            print("Before you continue please register with us")
            u_id = None
            u_n = input("User Name: ")
            u_p = input("password: ")
            c_n = input("Company Name: ")

            new_company = Other_user(user_id = u_id, user_name = u_n, user_password = u_p, company_name = c_n) 
            session.add(new_company)
            session.commit()
            
            # will add the log in code here  



                

