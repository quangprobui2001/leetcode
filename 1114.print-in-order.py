#
# @lc app=leetcode id=1114 lang=python
#
# [1114] Print in Order
#

# @lc code=start
from threading import Lock
class Foo(object):
    def __init__(self):
        self.firstDone = Lock()
        self.secondDone = Lock()
        self.firstDone.acquire()
        self.secondDone.acquire()


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        printFirst()
        self.firstDone.release()
        # printFirst() outputs "first". Do not change or remove this line.


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.firstDone.acquire()
        printSecond()
        self.secondDone.release()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.secondDone.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
# @lc code=end

