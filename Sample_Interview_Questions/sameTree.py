# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False
        stack_p = []
        stack_q = []
        node_p = []
        node_q = []
        stack_p.append(p)
        stack_q.append(q)
        while len(stack_p)>0:
            top = stack_p.pop()
            node_p.append(top.val)
            if top.left!=None:
                stack_p.append(top.left)
            else:
                node_p.append(-1)
            if top.right!=None:
                stack_p.append(top.right)
            else:
                node_p.append(-2)
        while len(stack_q)>0:
            top = stack_q.pop()
            node_q.append(top.val)
            if top.left!=None:
                stack_q.append(top.left)
            else:
                node_q.append(-1)
            if top.right!=None:
                stack_q.append(top.right)
            else:
                node_q.append(-2)                
        if len(node_p)!=len(node_q):
            return False
        return node_p==node_q
