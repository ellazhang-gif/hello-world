import random

class MinMaxQueue:
    def __init__(self, l):
        l.sort()
        self.sorted_q = l

    def pop_min(self):
        #perform on the min
        #------your code here -----#
        return self.sorted_q.pop(0)



        #------end of your code----#

    def pop_max(self):
        #perform on the max
        #------your code here -----#
        return self.sorted_q.pop()



        #------end of your code----#

def tester(n=10):
    #create the lists of integers and signs, respectively
    PseudoRandomGen = random.Random(0)
    num_int = n
    li = [PseudoRandomGen.randint(0, 20) for i in range(num_int)]
    print(li)
    li = list(set(li))
    sign_array = ["<" if PseudoRandomGen.randint(0, 1) else ">" for i in range(len(li) - 1)]
    mmq = MinMaxQueue(li)

    result = []
    #decide if you'd take out the min or max of the integer list
    #and append corresponding sign after it
    #------your code here -----#
    for i in sign_array:
        if i=="<":
            result.append(mmq.pop_min())
            result.append(i)
        else:
            result.append(mmq.pop_max())
            result.append(i)
    if sign_array[-1]=="<":
        result.append(mmq.pop_max())
    else:
        result.append(mmq.pop_min())





    #------end of your code----#
    print (result)
    return result
'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call below, if you are submitting for auto grading.
'''

'''
if __name__ == '__main__':
    tester()
    tester(2)
    tester(5)
'''
###I want to change this###
