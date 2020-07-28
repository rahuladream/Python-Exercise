class A:
    def explore(self):
        print("explore() method from class A")
    

class B(A):
    def explore(self):
        print("explore() method from class B")


if __name__ == '__main__':
    b_obj = B()
    a_obj = A()

    b_obj.explore()
    a_obj.explore()