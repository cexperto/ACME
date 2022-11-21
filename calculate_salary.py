from validate import ValidateHour
from datetime import datetime
import json


class CalculateSalaryEmploye:
    validate = ValidateHour()

    def format_hour(self, hour):
        validate = self.validate
        if not validate.validate_hour(hour) or not validate.validate_number(hour):
            return False
        
        return datetime.strptime(hour, "%H:%M").time()

    def calculate_time(self, end_hour, start_hour):
        return int(start_hour)-int(end_hour)
    
    def calculate_value_hours(self, day, start_hour, end_hour):
        start_hour = self.format_hour(start_hour)
        end_hour = self.format_hour(end_hour)
        if not start_hour or not end_hour:
            return json.dumps({'error': 'Invalid hour'})

        week_days = ['MO', 'TU', 'WE', 'TH', 'FR']
        weekend_days = ['SA', 'SU']
        values = {}
        if day in week_days:
            values['a'] = 25
            values['b'] = 15
            values['c'] = 20
        if day in weekend_days:
            values['a'] = 30
            values['b'] = 20
            values['c'] = 25
        
        num1 = str(start_hour)[0:2]
        num2 = str(end_hour)[0:2]
        
        if start_hour >= self.format_hour("00:01") and end_hour <= self.format_hour("09:00"):
            return self.calculate_time(num1, num2)*values['a']
        if start_hour >= self.format_hour("09:01") and end_hour <= self.format_hour("18:00"):
            return self.calculate_time(num1, num2)*values['b']
        if start_hour >= self.format_hour("18:01"):
            return self.calculate_time(num1, num2)*values['c']

    def calculate_salary(self, data):
        """ Take a dict with day and theirs hours, returns sum of values, total salary """
        sum_salary = []
        for k, v in data.items():
            sum_salary.append(self.calculate_value_hours(k, v[0], v[1]))
        return sum(sum_salary)
