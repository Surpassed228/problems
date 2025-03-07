class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    	if head == None or head.next == None:
    		return head

    	list_of_twos = []
    	current_head = head

    	while current_head != None and current_head.next != None:
    		to_change = current_head.next

    		current_head.next = to_change.next
    		to_change.next = current_head

    		list_of_twos.append(to_change)
    		list_of_twos.append(to_change.next)
    		current_head = list_of_twos[-1].next

    	the_head = list_of_twos[0]
    	head_list = [the_head]
    	for ind in range(1,len(list_of_twos)):
    		head_list[-1].next = list_of_twos[ind]
    		head_list.append(head_list[-1].next)

    	return the_head