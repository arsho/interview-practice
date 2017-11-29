# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    ar = []
    while l1:
        ar.append(l1.value)
        l1 = l1.next
    while l2:
        ar.append(l2.value)
        l2 = l2.next
    return sorted(ar)
