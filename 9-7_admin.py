class User():
    """User info"""
    def __init__(self, first_name, last_name, age):
        """User first name, last name, and age"""
        self.first = first_name
        self.last = last_name
        self.age = age

    def describe_user(self):
        print('First name: ' + self.first.title())
        print('Last name: ' + self.last.title())
        print('Age : ' + str(self.age))

    def greet_user(self):
        print("How are you doing today " + self.first.title()
              + " " + self.last.title() + "?")

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

new_user = Admin('ian', 'mcdonald', 30)
new_user.show_privileges()
new_user.greet_user()
new_user.describe_user()
