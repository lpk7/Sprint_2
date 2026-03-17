class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        work_hours = (7 - rest_days) * 8
        return cls(name, work_hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        new_email = f'{name}@email.com'
        return cls(name, hours, rest_days, new_email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        salary = self.hours * self.hourly_payment
        return salary