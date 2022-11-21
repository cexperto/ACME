class ValidateHour:
    """Class alidate hour, just allows numbers or in corrcets time ranges"""

    def validate_number(self, num):
        num1 = num[0:2]
        num2 = num[3:5]
        if (not num1.isnumeric() or
            not num2.isnumeric() or
            num[2] != ':'):
            return False
        return True

    def validate_hour(self, hour):
        hour = str(hour)
        if (len(hour) != 5 or
            int(hour[0:2]) >= 24 or
            int(hour[3:5]) > 59):
            return False
        return True
