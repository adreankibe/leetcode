class Solution(object):
    def reverseList(self, head):
        previous_node = None
        current_node = head
        
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_nped = next_node
        return previous_node
