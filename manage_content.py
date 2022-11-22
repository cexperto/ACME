class ManageContent:
    """ Class content functions to get info from str with above structure:
        RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
     """

    def __init__(self, data):
        self.data = data

    def get_name_employe(self):
        return self.data.split(sep='=')[0]

    def get_hour_init_hour_end(self, str):
        """10:00-12:00"""
        return str.split(sep='-')

    def get_turns_employe(self):
        employe = {}        
        employe['name'] = self.get_name_employe()
        data = self.data.split(sep='=').pop().split(',')
        for i in data:
            get_hours = self.get_hour_init_hour_end(i[2::])
            employe[i[0:2]] = get_hours
        return employe

