#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):
    if t==None:
        return []
    queue = []
    queue.append(t)
    ar = []
    while len(queue)>0:
        first = queue[0]
        del queue[0]
        if first.left != None:
            queue.append(first.left)
        if first.right!=None:
            queue.append(first.right)
        ar.append(first.value)
    return ar
