import random as rand

class employee:
    def __init__(self, employeeid, jobtitle, monthlyincome, name):
        self.__employeeid = employeeid
        self.__jobtitle = jobtitle
        self.__monthlyincome = monthlyincome
        self.__name = name
    
    def get_employeeid(self):
        return self.__employeeid
    
    def get_jobtitle(self): 
        return self.__jobtitle

    def get_monthlyincome(self):
        return self.__monthlyincome
        
    def get_name(self): 
        return self.__name

    def print_info(self):
        #print(f'Employee Name: {emp_name.get_name()}\n{emp_name.get_employeeid()}\nJob Title: {emp_name.get_jobtitle()}\nMonthlyIncome: {emp_name.get_monthlyincome()}\n')
        return '\nEmployee Name: ' + self.get_name() + \
               '\nEmployee ID: ' + str(self.get_employeeid()) + \
               '\nJob Title: ' + str(self.get_jobtitle()) + \
               '\nMonthly Income: ' + str(self.get_monthlyincome())

    def print_info2(self):
        #print(f'Employee Name: {emp_name.get_name()}\n{emp_name.get_employeeid()}\nJob Title: {emp_name.get_jobtitle()}\nMonthlyIncome: {emp_name.get_monthlyincome()}\n')
        return '\nEmployee ID: ' + str(self.get_employeeid()) + \
               '\nJob Title: ' + str(self.get_jobtitle()) + \
               '\nMonthly Income: ' + str(self.get_monthlyincome())

    def print_info3(self):
        #print(f'Employee Name: {emp_name.get_name()}\n{emp_name.get_employeeid()}\nJob Title: {emp_name.get_jobtitle()}\nMonthlyIncome: {emp_name.get_monthlyincome()}\n')
        return '\nEmployee ID: ' + str(self.get_employeeid()) + \
               '\nJob Title: ' + str(self.get_jobtitle())
    
    
def main():
    employeeID = []
    employees = ["Jack", "John", "Moses", "April", "May", "Jen", "June", "Sam", "Charles", "Greg"]
    
    for x in range(10):
        randm = int(rand.random() * 10000)
        employeerand = (f'EmployeeID_{randm}')
        employeerand = employee(employeerand, "Datacenter Technician", 4500, employees[x])
        employeeID.append(employeerand)
    
    for i in range(10):
        print(employeeID[i].print_info())
        
    for i in range(10):
        print(employeeID[i].print_info2())
        
    for i in range(10):
        print(employeeID[i].print_info3())
    

if __name__ == "__main__":
            main()
