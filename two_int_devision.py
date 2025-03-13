class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    	if numerator == 0:
    		return '0'
    	else:
    		beginning = ''
    		x = numerator < 0
    		y = denominator < 0
    		neg = True if ((not x and y) or (not y and x)) else False
    		numerator,denominator = abs(numerator),abs(denominator)
    		beginning += f'-{numerator//denominator}.' if neg else f'{numerator//denominator}.'
    		remainder = numerator - numerator//denominator*denominator
    		if remainder == 0:
    			return beginning[:-1]
    		else:
    			check_list = [remainder]
    			while check_list[-1]//denominator == 0:
    				check_list.append(int(str(check_list[-1])+'0'))
    			
    			num_zeros = len(check_list) - 2
    			beginning += ''.join([str(0) for _ in range(num_zeros)])

    			dev_alg_nums = check_list
    			to_str_nums = ['0' for _ in range(num_zeros)]

    			while dev_alg_nums[-1] != 0 and dev_alg_nums[-1] not in dev_alg_nums[:-1]:
    				Z = dev_alg_nums[-1]//denominator
    				to_str_nums.append(str(Z))
    				next_num = dev_alg_nums[-1] - Z*denominator
    				dev_alg_nums.append(int(str(next_num) + '0') if next_num != 0 else next_num)

    			if dev_alg_nums[-1] == 0:
    				beginning += ''.join(to_str_nums[num_zeros:])
    			else:
    				stop_ind = None
    				for back_ind in range(-2,-len(dev_alg_nums),-1):
    					if dev_alg_nums[back_ind] == dev_alg_nums[-1]:
    						stop_ind = back_ind
    						break
    				stop_ind = len(dev_alg_nums) + stop_ind - 1
    				beginning = beginning[:-num_zeros] if num_zeros != 0 else beginning
    				to_str_nums = to_str_nums[:stop_ind] + ['('] + to_str_nums[stop_ind:] + [')']
    				beginning += ''.join(to_str_nums)

    			return beginning



