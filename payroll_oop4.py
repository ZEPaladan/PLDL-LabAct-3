#This program will simple access the codes under payroll_oop2.py
#Thhis program will compute partial deductiopn of the employee

import payroll_oop2 #Calling the payroll_oop2.py

#Instantiate payroll_oop2.py and place it inside the employee_payroll. Note: employee_payroll is changeable as you wish
employee_payroll = payroll_oop2.Emmployee_Salary()
emp_rate_per_hour = float(input("Enter value for rate per hour: "))
emp_num_of_absences = int(input("Enter value for number of absences: "))
tardiness_hours = int(input("Enter number of tardiness: "))

#Accessing the codes under attribute get_absences_deduction inside the Employee_Salary class.
absences_deduction = employee_payroll.get_absences_deduction(emp_rate_per_hour, emp_num_of_absences)
tardiness_deduction = employee_payroll.get_tardiness_deduction(emp_rate_per_hour, tardiness_hours)

#Formula to compute partial deduction of an employee
partial_deduction = absences_deduction + tardiness_deduction
print("Employee partial deduction is: %.2f" % partial_deduction)