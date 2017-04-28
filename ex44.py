class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

class Parent1(object):

    def override(self):
        print("PARENT override()")