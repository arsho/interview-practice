# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    ar = []
    head = l
    while head != None:
        if head.value != k:
            ar.append(head.value)
        head = head.next
    return ar
