
class Post:
    def __init__(self, username, password):
        self.username = username
        self.password = password


p = Post("ssar", "1234")

print(p.__dict__)
