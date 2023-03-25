class User:
    id = None
    name = None
    firstname = None
    pseudo = None
    password = None

    def __init__(self, id, name, firstname, pseudo, password):
        self.id = id
        self.name = name
        self.firstname = firstname
        self.pseudo = pseudo
        self.password = password
