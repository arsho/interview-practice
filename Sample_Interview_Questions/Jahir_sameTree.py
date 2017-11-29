def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            x,y=[],[]
            m,n=[p],[q]
            while m and n:
                e=m.pop(0)
                f=n.pop(0)
                l,r=1,1
                if e.val!=f.val:
                    return False
                if e.left and f.left:
                    m+=[e.left]
                    n+=[f.left]
                    l=0
                if e.right and f.right:
                    m+=[e.right]
                    n+=[f.right]
                    r=0
                if l==1 and (e.left or f.left):
                    return False
                if r==1 and (e.right or f.right):
                    return False 
return True
