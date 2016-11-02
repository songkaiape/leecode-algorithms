
#Given a linked list, swap every two adjacent nodes and return its head.

#For example,
#Given 1->2->3->4, you should return the list as 2->1->4->3.

#Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

class solution(object):
  def swapPairs(self,head):
    pre,pre.next=self,head
    while pre.next and pre.next.next:
      a=pre.next
      b=a.next
      pre.next,b.next,a.next=b,a,b.next
      pre=a
    return self.next
  #recursive
  def swapPairs2(self,head):
    if head!=None and head.next!=None:
      next=head.next
      head,next=self.swapPairs2(next.next)
      next.next=head
      return next
