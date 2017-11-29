def searchInsert(self, nums, target):

       #First way of solution...................
       '''
        l=len(nums)
        x=[i for i in range(l) if nums[i]>=target]
        if x==[]:
            return l
         return x[0]
        '''
        #second way of solution.......
        x=len(nums)
        s,e=0,x
        while s<e:
            x=(s+e)//2
            if  nums[x]<target:
                s=x+1
            if nums[x]>target:
                e=x
            if nums[x]==target:
                return x
return s
