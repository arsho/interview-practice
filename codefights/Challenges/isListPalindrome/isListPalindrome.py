# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    ar = []
    while l:
        x=l.value
        ar.append(x)
        l=l.next
    return ar == ar[::-1]
