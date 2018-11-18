class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


    def preorder(self, data):
        if data:
            print(data.data)
            self.preorder(data.left)
            self.preorder(data.right)

    def inorder(self, data):
        if data:
            self.inorder(data.left)
            print(data.data)
            self.inorder(data.right)

    def postorder(self, data):
        if data:
            self.postorder(data.left)
            self.postorder(data.right)
            print(data.data)

def main():
    data = Node(11)
    data.insert(12)
    data.insert(22)
    data.insert(55)
    data.insert(33)
    data.insert(3)
    data.insert(2)
    data.insert(43)
    data.insert(54)
    print "**Preordered Binary Tree Traversal**"
    data.preorder(data)
    print "............."
    print "**Inordered Binary Tree Traversal**"
    data.preorder(data)
    print ".............."
    print "**Postordered Binary Tree Traversal**"
    data.preorder(data)
    print "..............."


main()
