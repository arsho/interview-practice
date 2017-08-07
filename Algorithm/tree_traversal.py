'''
         1
        / \
       /   \
      /     \
     2       3
    / \     /
   4   5   6
  /       / \
 7       8   9
'''


class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_tree():
    t = Tree(1)
    t.left = Tree(2)
    t.left.left = Tree(4)
    t.left.right = Tree(5)
    t.left.left.left = Tree(7)
    t.right = Tree(3)
    t.right.left = Tree(6)
    t.right.left.left = Tree(8)
    t.right.left.right = Tree(9)
    return t

def pre_order(node):
    if node is not None:
        print(node.value,end=" ")
        pre_order(node.left)
        pre_order(node.right)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.value, end=" ")
        in_order(node.right)

if __name__ == '__main__':
    t = create_tree()
    print("Pre Order: ",end = "")
    pre_order(t)

    print()

    print("In Order: ",end = "")
    in_order(t)
