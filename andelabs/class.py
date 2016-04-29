class Car(object):
    def __init__(self, name='', model='', *args):
        self.models = args
        self.model = model if len(model) > 0 else 'GM'
        self.name = name if len(name) > 0 else 'General'
        self.num_of_doors = 4 if not(self.name =='Porshe' or self.name == 'Koenigsegg') else 2
        self.num_of_wheels = 8 if 'trailer' in self.models else 4 
        self.speed = 0;

    def is_saloon(self):
        if self.model is not 'trailer':
            return True
        else:
            return False 

    def drive(self, num):
        if self.model == 'trailer' or 'trailer' in self.models:
            self.speed = num * 11
        if self.name == 'Mercedes':
            self.speed = 10**num
        return self