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


class Parent2(object):

    def altered(self):
        print("PARENT altered()")

class Child2(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad2 = Parent2()
son2 = Child2()

dad2.altered()
son2.altered()

