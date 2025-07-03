class User :
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"the user full  name is {self.first_name} {self.last_name}")
    
    def greet_user(self):
        print(f" good afternoon {self.first_name}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# class Privileges:
#     def __init__(self):
#         self.privileges = ["can add post","can delete post","can ban user"] 
    
#     def show_privileges(self):
#         print("Privileges: ")

#         for privilege in self.privileges:
#             print(f"-{privilege}")


# class Admin(User):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name) 
#         self.privileges = Privileges() # attribute of privileges class 

