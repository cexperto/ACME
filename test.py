import unittest
import unittest.mock
import datetime
import io
import sys
from read_files import ReadFiles
from manage_content import ManageContent
from calculate_salary import CalculateSalaryEmploye
from validate import ValidateHour
from main import EmployeesAcme


class TestReadFiles(unittest.TestCase):
    
    mock_file_content = """RENE=MO10:00-12:00"""
    
    def test_read_files(self):
        with unittest.mock.patch(
                'builtins.open',
                new=unittest.mock.mock_open(read_data=self.mock_file_content),
                create=True
        ) as _:            
            expected = '{"error": "The file should with at least five sets of data"}'
            self.assertEqual(ReadFiles('/').read_files(), expected)
            self.assertEqual(type(ReadFiles('/').read_files()), str)


class TestManageContent(unittest.TestCase):
    data = "PABLO=MO10:00-12:00"
    manage = ManageContent(data)
    
    def test_get_name(self):
        self.assertEqual(self.manage.get_name_employe(), 'PABLO')

    def test_get_hour_init_hour_end(self):
        self.assertEqual(self.manage.get_hour_init_hour_end(self.data[8::]), ["10:00","12:00"])

    def test_get_turns_employe(self):
        self.assertEqual(type(self.manage.get_turns_employe()), dict)
        self.assertEqual(self.manage.get_turns_employe()['name'], 'PABLO')


class TestCalculateSalary(unittest.TestCase):
    calculate_salary = CalculateSalaryEmploye()

    def test_format_hour(self):
        format_true = self.calculate_salary.format_hour("00:01")
        format_false = self.calculate_salary.format_hour("01")
        self.assertEqual(type(format_true), datetime.time)
        self.assertEqual(format_false, False)

    def test_calculate_time(self):
        start_hour, end_hour = "12", "10"
        c_time = self.calculate_salary.calculate_time(end_hour, start_hour)
        self.assertEqual(c_time, 2)

    def test_calculate_value_hours(self):
        day1 = 'MO'
        day2 = 'SA'
        start_hour = "10:00"
        end_hour = "12:00"
        c_v_h = self.calculate_salary.calculate_value_hours(day1, start_hour, end_hour)
        c_v_h1 = self.calculate_salary.calculate_value_hours(day2, start_hour, end_hour)
        self.assertEqual(c_v_h, 30)
        self.assertEqual(c_v_h1, 40)

    def test_calculate_salary(self):
        data = {'MO': ['10:00', '12:00'], 'TH': ['12:00', '14:00'], 'SU': ['20:00', '21:00']}
        salary = self.calculate_salary.calculate_salary(data)
        self.assertEqual(salary, 85)

        
class TestValidateHour(unittest.TestCase):
    
    validate = ValidateHour()

    def test_validate_number(self):
        v_n_true = self.validate.validate_number("12:00")
        v_n_false = self.validate.validate_number("aa:00")
        self.assertEqual(v_n_true, True)
        self.assertEqual(v_n_false, False)

    def test_validate_hour(self):
        v_h_true = self.validate.validate_hour("12:00")
        v_h_false = self.validate.validate_hour("24:00")
        self.assertEqual(v_h_true, True)
        self.assertEqual(v_h_false, False)


class TestEmployeesAcme(unittest.TestCase):

    main = EmployeesAcme()

    def test_get_data(self):
        data_mock = TestReadFiles.mock_file_content
        get_data = self.main.get_data(data_mock)
        self.assertEqual(type(get_data), list)
    
    def test_caculate_salary(self):
        expected_result = 'The amount to pay DIANA is: 80 USD\nThe amount to pay ASTRID is: 60 USD\n'
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        data = [{'name': 'DIANA', 'SA': ['14:00', '18:00']}, 
                {'name': 'ASTRID', 'MO': ['10:00', '12:00'], 
                'TH': ['12:00', '14:00']}]
        self.main.salary_employes(data)
        sys.stdout = sys.__stdout__
        result = capturedOutput.getvalue()
        self.assertEqual(type(result), str)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()