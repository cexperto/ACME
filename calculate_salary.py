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

    def calculate_time(self, hour_end, hour_start):
        return int(hour_start)-int(hour_end)
    
    def calculate_hours(self, day, hour_start, hour_end):
        hour_start = self.format_hour(hour_start)
        hour_end = self.format_hour(hour_end)
        if not hour_start or not hour_end:
            return json.dumps({'error': 'hour invalid'})

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
        
        num1 = str(hour_start)[0:2]
        num2 = str(hour_end)[0:2]
        
        if hour_start >= self.format_hour("00:01") and hour_end <= self.format_hour("09:00"):
            return self.calculate_time(num1, num2)*values['a']
        if hour_start >= self.format_hour("09:01") and hour_end <= self.format_hour("18:00"):
            return self.calculate_time(num1, num2)*values['b']
        if hour_start >= self.format_hour("18:01"):
            return self.calculate_time(num1, num2)*values['c']

    def calculate_salary(self, data):
        sum_salary = []
        for k, v in data.items():
            sum_salary.append(self.calculate_hours(k, v[0], v[1]))
        return sum(sum_salary)
