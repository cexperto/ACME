from read_files import ReadFiles
from manage_content import ManageContent
from calculate_salary import CalculateSalaryEmploye


class EmployeesAcme:

    def get_data(self, content):
        data = []
        for i in content:
            manage = ManageContent(i)
            data.append(manage.get_turns_employe())
        return data
    
    def salary_employes(self, data):
        for data in data:
            name = data['name']
            data.pop('name')
            salary = CalculateSalaryEmploye().calculate_salary(data)
            print(f'The amount to pay {name} is: {salary} USD')


if __name__ == '__main__':
    name_file = "employes.txt"
    read = ReadFiles(name_file).read_files()
    data = EmployeesAcme().get_data(read)
    EmployeesAcme().salary_employes(data)
