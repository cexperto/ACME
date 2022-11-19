from read_files import ReadFiles
from manage_content import ManageContent
from calculate_salary import CalculateSalaryEmploye


class EmployeesAcme:

    read = ReadFiles("employes.txt").read_files()

    def get_data(self):
        data = []
        for i in self.read:
            manage = ManageContent(i)
            data.append(manage.get_turns_employe())
        return data
    
    def salary_employes(self):
        set_data = self.get_data()
        for data in set_data:
            name = data['name']
            data.pop('name')
            salary = CalculateSalaryEmploye().calculate_salary(data)
            print(f'The amount to pay {name} is: {salary} USD')


if __name__ == '__main__':
    EmployeesAcme().salary_employes()
