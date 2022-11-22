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
        num1 = str(start_hour)[0:2]
        num2 = str(end_hour)[0:2]
        start_first_range = self.format_hour("00:01")
        end_first_range = self.format_hour("09:00")
        start_sec_range = self.format_hour("09:01")
        end_sec_range = self.format_hour("18:00")
        start_third_range = self.format_hour("18:01")

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
        
        if (start_hour >= start_first_range and
            start_hour < end_first_range and
            end_hour > end_first_range and
            end_hour < start_third_range):
            hour_range2 = self.calculate_time(9, num2)
            hour_range1 = self.calculate_time(hour_range2, num2)
            
            return hour_range2*values['b']+hour_range1*values['a']
            
        if (start_hour >= start_first_range and
            start_hour < start_sec_range and
            end_hour > start_third_range):

            hour_range1 = self.calculate_time(num1, 9)*values['a']
            hour_range2 = self.calculate_time(18, num2)*values['c']            
            return hour_range1+hour_range2+(9*values['b'])
            
        if (start_hour >= start_sec_range and
            start_hour <= end_sec_range and
            end_hour > start_third_range):

            hour_range1 = self.calculate_time(num1, 18)*values['b']
            hour_range2 = self.calculate_time(18, num2)*values['c']            
            return hour_range2+hour_range1


        if start_hour >= start_first_range and end_hour <= end_first_range:
            return self.calculate_time(num1, num2)*values['a']
        if start_hour >= start_sec_range and end_hour <= end_sec_range:
            return self.calculate_time(num1, num2)*values['b']
        if start_hour >= start_third_range:
            return self.calculate_time(num1, num2)*values['c']

    def calculate_salary(self, data):
        """ Take a dict with day and theirs hours, returns sum of values, total salary """
        try:
            sum_salary = []
            for k, v in data.items():
                sum_salary.append(self.calculate_value_hours(k, v[0], v[1]))
            return sum(sum_salary)
        except Exception as e:
            return e
