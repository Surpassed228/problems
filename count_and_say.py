#RLE('nums') changes digits to count_consecutive,digit num -> count|num
#Count_and_say sequence is x1 = '1' .... xn = RLE(x_n-1) ... 
#need to return the n'th element of a sequence
#RLE takes strings and main_function takes integers 

class Solution:
    def RLE(self,some_string):
        count_list = []
        values_list = []
        count = 0
        current_char = some_string[0]

        for char in some_string:
            if current_char != char:
                count_list.append(str(count))
                values_list.append(current_char)
                count = 1
            else:
                count += 1
            current_char = char

        if len(values_list) == 0 or values_list[-1] != current_char:
            values_list.append(current_char)
            count_list.append(str(count))

        join_list = []
        for ind in range(len(count_list)):
            join_list.extend([count_list[ind],values_list[ind]])

        return ''.join(join_list)

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            return self.RLE(self.countAndSay(n-1))


