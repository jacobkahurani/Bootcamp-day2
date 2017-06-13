class Car(object):
    def __init__(self,name="General",model="GM",type="saloon"):
        self.__name = name
        self.__model = model
        self.__type = type
        doors = 4
        wheels = 4
        speed = 0
        self.speed = speed
        self.num_of_doors = doors
        self.num_of_wheels = wheels
    def get_name(self): 
        return self.__name
    def get_model(self):
        return self.__model
    def set_name(self,Name):
        self.__name = Name
        if self.__name == "Porshe" or self.__name == "Koenigsegg":
            self.num_of_doors = 2
    def set_model(self,Model):
        self.__model = Model
    def get_type(self):
        return self.__type
    def set_type(self,Type):
        self.__type = Type
        if self.__type == "trailer":
            self.num_of_wheels = 8
    def drive(self,gear):
        if self.__type == "saloon":
            self.speed = gear * 333.3333333
        else:
            self.speed = gear * 11
    type = property(get_type,set_type)
    name = property(get_name,set_name)
    model = property(get_model,set_model)
