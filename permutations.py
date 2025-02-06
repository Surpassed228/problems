class Solution:

    def nextPermutation(self, nums: list[int]) -> None:
        if len(nums) != 1 and not self.same(nums):
            #the simplest case is [a1,a2] where a1>a2 or a2<a1
            count = []
            self.N(nums,cnt = count)
            if len(count) == len(nums):
                nums.sort()

    def N(self,the_list,cnt,curr_ind = 0):
        if len(the_list[curr_ind:]) == 1:
            cnt.append(1)
        elif the_list[curr_ind:][0] != max(the_list[curr_ind:]):
            if self.is_max(the_list[curr_ind:][1:]):
                the_next = self.get_next(the_list[curr_ind:][0],the_list[curr_ind:][1:]) #is index of the next largest
                the_list[curr_ind + 0],the_list[curr_ind + the_next] = the_list[curr_ind + the_next],the_list[curr_ind + 0]
                self.ins_sort(the_list,from_ind = curr_ind+1)
            else:
                cnt.append(1)
                self.N(the_list,cnt = cnt,curr_ind = curr_ind + 1)
        else:
            cnt.append(1)
            self.N(the_list,cnt = cnt,curr_ind = curr_ind + 1)

    def ins_sort(self,AA,from_ind = 1):
        #from_ind is non-negative integer
        N = len(AA)
        for j in range(from_ind+1,N):
            key = AA[j]
            i = j-1
            while i>=from_ind and AA[i] > key:
                AA[i+1] = AA[i]
                i -= 1
            AA[i+1] = key

    def lin_search(self,B,lst):
        for ind in range(len(lst)):
            if lst[ind] == B:
                return ind + 1

    def get_next(self,A,lst):
        the_next = A + 1
        while the_next not in lst:
            the_next += 1
        return self.lin_search(the_next,lst)

    def is_max(self,lst):
        if len(lst) == 1:
            return True
        elif len(lst) == 2:
            return True if lst[0] == max(lst) else False
        else:
            return True if lst[0] == max(lst) and self.is_max(lst[1:]) else False

    def same(self,the_list):
        #len(the_list) > 2
        first = the_list[0]
        for item in the_list:
            if item != first:
                return False
        return True
                


