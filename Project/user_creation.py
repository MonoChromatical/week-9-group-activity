# Nonoka-T
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f'{self.name} {self.role}'


# admin
class Admin:
    def __init__(self, name):
        self.name = name
        self.role = 'admin'


# editor
class Editor(User):
    def __init__(self, name):
        self.name = name
        self.role = 'editor'


# viewer
class Viewer(User):
    def __init__(self, name):
        self.name = name
        self.role = 'viewer'


def create_user(user_type, name):
    if user_type == 'admin':
        return Admin(name)

    elif user_type == 'editor':
        return Editor(name)

    elif user_type == 'viewer':
        return Viewer(name)

    else:
        print("Invalid user type")
        return None


if __name__ == '__main__':
    user1 = create_user('admin', 'Cameron')
    user2 = create_user('editor', 'Sophie')
    user3 = create_user('viewer', 'Nonoka')
    user4 = create_user('viewer', 'Ashton')

    print(user1)
    print(user2)
    print(user3)
    print(user4)
