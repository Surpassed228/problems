class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        #variables that we are going to change
        one = l1
        two = l2
        sum_number = []
        #value to remember
        rem = 0
        while one.next != None or two.next != None:
            the_value = one.val + two.val + rem
            to_list_value = the_value%10 

            #add a new value
            sum_number.append(ListNode(to_list_value))

            rem = the_value//10

            bad_value = one if one.next == None else (two if two.next == None else None)
            if bad_value == one:
                one.next = ListNode()
            elif bad_value == two:
                two.next = ListNode()
            else:
                pass

            #update all the variable
            one = one.next
            two = two.next
        #manage the ramaining value 
        last_value = one.val + two.val + rem
        first = last_value%10
        second = last_value//10

        #insert the last value
        if second == 0:
            sum_number.append(ListNode(first))
        elif second == 1:
            sum_number.append(ListNode(first))
            sum_number.append(ListNode(second))

        if len(sum_number) == 1:
            return sum_number[0]
        else:
            for ind in range(len(sum_number)-1):
                sum_number[ind].next = sum_number[ind+1]
            return sum_number[0]