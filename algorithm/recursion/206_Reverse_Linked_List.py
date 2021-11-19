class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Base Case:
        if not head or not head.next:
            #not head: means this is empty linked list initally
            #not head.next: means this is the last node in the linked list
            return head
        #Recursive Case:
        #rhead in this case will be the last node in the original linked list
        rhead = self.reverseList(head.next)
        
        #head, in this case, will be the second last node
        #head.next = last node, (head.next).next = head, meaning change the pointer of last node to the second last node (head)
        head.next.next = head
        #break the connection of second last node (head) with the last node
        #by doing head.next = None
        head.next = None
        #Return the rhead, which is last node in the original linked list 
        
        return rhead 
