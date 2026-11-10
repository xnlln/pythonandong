def calculate_basic_salary(time_rendered, rate_per_hour):
    return time_rendered * rate_per_hour

def calculate_total_deductions(sss, pagibig, philhealth):
    return sss + pagibig + philhealth

def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance

def calculate_net_salary(gross_salary, total_deductions):
    return gross_salary - total_deductions

def display_salary_info(name, time_rendered, rate_per_hour, basic_salary, allowance, sss, pagibig, philhealth, total_deductions, gross_salary, net_salary):
    print("\n========================================")
    print("       EMPLOYEE SALARY CALCULATOR       ")
    print("========================================")
    
    print(f"\nEmployee Name      : {name}")
    print(f"Time Rendered      : {time_rendered:g} hours")
    print(f"Rate per Hour      : ₱{rate_per_hour:,.2f}")
    
    print(f"\nBasic Salary       : ₱{basic_salary:,.2f}")
    print(f"Allowance          : ₱{allowance:,.2f}")
    
    print(f"\nDeductions:")
    print(f"  SSS              : ₱{sss:,.2f}")
    print(f"  Pag-IBIG         : ₱{pagibig:,.2f}")
    print(f"  PhilHealth       : ₱{philhealth:,.2f}")
    print(f"  Total Deductions : ₱{total_deductions:,.2f}")
    
    print(f"\nGross Salary       : ₱{gross_salary:,.2f}")
    print(f"Net Salary         : ₱{net_salary:,.2f}")
    print("========================================")

def main():
    print("--- Enter Employee Information ---")
    name = input("Employee Full Name: ")
    time_rendered = float(input("Time Rendered (hours): "))
    rate_per_hour = float(input("Rate per Hour: "))
    allowance = float(input("Allowance: "))
    
    print("\n--- Enter Deductions ---")
    sss = float(input("SSS Deduction: "))
    pagibig = float(input("Pag-IBIG Deduction: "))
    philhealth = float(input("PhilHealth Deduction: "))

    basic_salary = calculate_basic_salary(time_rendered, rate_per_hour)
    total_deductions = calculate_total_deductions(sss, pagibig, philhealth)
    gross_salary = calculate_gross_salary(basic_salary, allowance)
    net_salary = calculate_net_salary(gross_salary, total_deductions)

    display_salary_info(name, time_rendered, rate_per_hour, basic_salary, allowance, sss, pagibig, philhealth, total_deductions, gross_salary, net_salary)

if __name__ == "__main__":
    main()