# Linked list example
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

# the lined list class

class LinkedList(object):
    def __init__(self, head=None):
        # self.count: int
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while(item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()

    def deleteAt(self, idx):
        if idx > self.count - 1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx - 1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1


    def dump_list(self):
        tempnode = self.head
        while(tempnode != None):
            print("Node :", tempnode.get_data())
            tempnode = tempnode.get_next()


itemlist = LinkedList()
itemlist.insert(27)
itemlist.insert(89)
itemlist.insert(100)
itemlist.dump_list()

# print("Item count", itemlist.get_count())
# print("finding item", itemlist.find(100))
# print("finding item", itemlist.find(121))

itemlist.deleteAt(2)
print("Item count", itemlist.get_count())
print("findinig item", itemlist.find(89))
itemlist.dump_list()
