from datetime import datetime


class Employee:

    def __init__(self,name,age,salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year =employment_year

    def __str__(self):
        return(f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()}')

    def get_working_years(self):
        year = int('2022')
        employment_year_int = int(self.employment_year)
        return year - employment_year_int
    

        


class Manager(Employee):

    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage



    def __str__(self):
        return(f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()}, Bonus: {self.get_bonus()}')


    def get_bonus(self):
        return float(self.bonus_percentage) * float(self.salary)
         

    
    
        
def main():
    non_managerial_employees = []
    managers = []

    print('Welcome to HR Pro 2022')
    print(
        f'Options:\n'
        f'\t1. Show Employees\n'
        f'\t2. Show Managers\n'
        f'\t3. Add An Employee\n'
        f'\t4. Add A Manager\n'
        f'\t5. Exit\n'
        )

    exit_program = False

    while exit_program == False: 

        selected_option = int(input("What would you like to do? "))

        if selected_option == 1:
            print("-----------------")
            print(f'Employees\n')
            for employee in non_managerial_employees:
                print(f'{employee}\n')
            print("-----------------")
    
        if selected_option == 2:
            print("-----------------")
            print(f'Managers\n')
            for employee in managers:
                print(f'{employee}\n')
            print("-----------------")

        if selected_option == 3:
            name = input("Name: ")
            age= input("Age: ")
            salary = input("Salary: ")
            employment_year = input("Employment Year: ")

            new_employee = Employee(name,age,salary,employment_year)
            non_managerial_employees.append(new_employee)
            print(
                f'Employee added succesfully'
            )      

        
        if selected_option == 4:
            name = input("Name: ")
            age= input("Age: ")
            salary = input("Salary: ")
            employment_year = input("Employment Year: ")
            bonus_percentage = input("Bonus Percentage: ")

            new_manager = Manager(name,age,salary,employment_year,bonus_percentage)
            managers.append(new_manager)
            print(
                f'Manager added succesfully'
            )      


        if selected_option == 5:
            exit_program = True


   

if __name__ == '__main__':
	main()
