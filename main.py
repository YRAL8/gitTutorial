class A:
    pass

class B:
    pass

class C(B):
    pass

class D(C,A):
    pass

class Verification:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError('Слабый пароль')

    def save(self):
        with open('user','a') as r:
            r.write(f'{self.login, self.password}' + '\n')










