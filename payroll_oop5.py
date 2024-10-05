#This program will compute the tardiness deduction nad overtime pay of an employee

import payroll_oop2

payroll = payroll_oop2.Emmployee_Salary()
emp_rate_per_hour = float(input("Enter the value for rate per hour: "))
emp_hour_overtime = float(input("Enter the number of hours work by the employee: "))
emp_hour_tardiness = float(input("Enter the number of tardiness iun hours by the employee: "))

tardiness_deduction = payroll.get_tardiness_deduction(emp_hour_tardiness, emp_rate_per_hour)
overtime_pay = payroll.get_overtime_pay(emp_hour_overtime, emp_rate_per_hour)

print("Employee tardiness deduction is: %.2f" % tardiness_deduction)
print("Employee overtime pay: %.2f" % overtime_pay)