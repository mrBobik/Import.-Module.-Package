from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
from pytime import pytime


a =[2,3,5]

if __name__ == '__main__':
    calculate_salary(a)
    get_employees()
    print(date.today())
    print(pytime.time_format(timestamp=None, format="%X"))

