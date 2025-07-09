import pandas as pd

class Employee:
    def __init__(self, name, title, salary, experience):
        self.name = name
        self.title = title
        self.salary = salary
        self.experience = experience
    
    def __str__(self):
        return f"Name = {self.name}, \nTitle = {self.title}, \nSalary = ${self.salary}, \nExperience = {self.experience} years"
    
    def to_dict(self):
        return {
            'name': self.name,
            'title': self.title,
            'salary': self.salary,
            'experience': self.experience
        }
def main():
    emp1 = Employee("Wally", "Manager", 10000, 4)    
    emp2 = Employee("Eva", "Engineer", 8000, 4)
    emp3 = Employee("Sam", "Engineer", 8000, 3)
    emp4 = Employee("Katie", "Engineer", 11000, 5)
    emp5 = Employee("Bob", "Engineer", 18000, 8)
    
    employee_array = []
    employee_array.append(emp1)
    employee_array.append(emp2)
    employee_array.append(emp3)
    employee_array.append(emp4)
    employee_array.append(emp5)
    
    print(employee_array[0])
    
    employee_dataframe = pd.DataFrame.from_records([emp.to_dict() for emp in employee_array])
    print(employee_dataframe)
#     How to get this in a fancy pandas way?
#     names_array = ["Wally", "Eva", "Sam", "Katie", "Bob"]
    names_array = []
    
    for e in employee_array:
        names_array.append(e.name)
    print(names_array)
    
    names = employee_dataframe['name'].to_frame()
    print("\n", names)
    
    employee_dataframe.index = names_array
    print(employee_dataframe)
    
    print(employee_dataframe.loc["Eva"])

if __name__ == "__main__":
    main()
