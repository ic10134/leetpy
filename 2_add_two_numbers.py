import ast

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:list, l2:list) -> list:
        dummy = ListNode()
        current = dummy
        carry = 0
        l1_index, l2_index = len(l1) - 1, len(l2) - 1
        
        while l1_index >= 0 or l2_index >= 0 or carry:
            x = l1[l1_index] if l1_index >= 0 else 0
            y = l2[l2_index] if l2_index >= 0 else 0
            s = x + y + carry
            carry = s // 10
            current.next = ListNode(s % 10)
            current = current.next
            l1_index -= 1
            l2_index -= 1
        
        res = []
        while dummy.next:
            res.append(dummy.next.val)
            dummy = dummy.next
        return res

if __name__ == '__main__':
    l1 = ast.literal_eval(input("Enter the elements of the array as first list: "))
    l2 = ast.literal_eval(input("Enter the elements of the array as second list: "))
    s = Solution()
    print(s.addTwoNumbers(l1, l2))