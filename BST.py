class BST:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data)

    def search(self, key):
        if self.data == key:
            print(f"\nNode {key} is present")
            return
        if key < self.data:
            if self.left is not None:
                self.left.search(key)
            else:
                print(f"\nNode {key} is not present in the tree")
        else:
            if self.right is not None:
                self.right.search(key)
            else:
                print(f"\nNode {key} is not present in the tree")

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right is not None:
            self.right.inorder()

    def preorder(self):
        print(self.data, end=" ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.data, end=" ")

#  Main 
root = BST(21)
list1 = [30,28, 6, 18, 63, 150, 1, 99]

for i in list1:
    root.insert(i)

print("\nTraversal - Inorder:")
root.inorder()
print("\nTraversal - Preorder:")
root.preorder()
print("\nTraversal - Postorder:")
root.postorder()

# Search example
root.search(30)


#  Graph 
import matplotlib.pyplot as p
import math

p.title('BFS-graph for asymptotic notation')
p.xlabel('Input Size')
p.ylabel('Steps (log2)')

x = list(range(1, 100))
y = [math.log2(i) for i in x]  # log2 is typical for BST complexity

p.plot(x, y, 'r', label='O(log n) - insert/delete/search')
p.legend()
p.show()
