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


class Child1(Parent):

    def override(self):
        print("CHILD override()")

dad1 = Parent1()
son1 = Child1()

dad1.override()
son1.override()

