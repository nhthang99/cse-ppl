class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    @property
    def do_something(self):
        print("Hi " + str(self))
    
if __name__ == "__main__":
    users = [User("nhthang99", "nhthang99@outlook.com"), User("thang", "thang@gmail.com")]
    for user in users:
        user.do_something