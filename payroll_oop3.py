#This program will compute the basic pay, honorarium pay, and absences deduction
import payroll_oop2

obj = payroll_oop2.Employee_Info()
company = input("Enter company name: ")
department = input("Enter employee department: ")
employee_name = input("Enter employee name: ")
employee_code = input("Enter employee number or code: ")
salary_cutoff = input("Enter salary cut-off: ")
emp_data = obj.get_emp_data(company, department, employee_name, employee_code, salary_cutoff)

#Data entry for basic pay computation
obj2 = payroll_oop2.Emmployee_Salary()
rate_pay = float(input("Enter employee rate per hour: "))
number_working_hours = float(input("Enter employee number of working hours: "))
honorarium_pay = float(input("Enter honorarium pay: "))
number_absences = float(input("Enter number of absences in hours: "))

#Computation for basic pay
basic_pay = obj2.get_basic_pay(rate_pay, number_working_hours)
absences_deduction = obj2.get_absences_deduction(rate_pay, number_absences)

#Display Output
print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")
obj.display_data()
print("Basic Pay: %.2f" % basic_pay)
print("Honorarium Pay: %.2f" % honorarium_pay)
print("Employee absences deduction: %.2f" % absences_deduction)
print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")
