class UserData:

    def __init__(self, first_name, last_name, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.city = city

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
