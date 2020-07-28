class A:
    def explore(self):
        print("explore() method from class A")

class B(A):
    def explore(self):
        super().explore()
        print("explore() method from class B")

if __name__ == '__main__':
    b_obj = B()
    b_obj.explore()