class Admin(User):
    """A class for describing an Admin"""
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.first = first_name
        self.last = last_name
        self.age = age
        self.privileges = ['can add post',
                           'can delete post',
                           'can ban user',]

    def show_privileges(self):
        print("Admins have the following privileges:")
        for privilege in self.privileges:
            print("\t-" + privilege)
