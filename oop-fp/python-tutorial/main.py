import hr
import employee
import productivity

manager = employee.Manager(1, 'Mary Poppins', 3000)
secretary = employee.Secretary(2, 'John Smith', 1500)
sales_guy = employee.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employee.FactoryWorker(2, 'Jane Doe', 40, 15)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
]
productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)