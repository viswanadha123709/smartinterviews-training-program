class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        class node():
            def __init__(self,data):
                self.data=data
                self.next=None
        head=node(0)
        temp=head
        dp=set()
        dp.add(0)
        for i in range(1,n+1):
            head.next=node(i)
            head=head.next
        head.next=temp
        
        while len(dp)<n:
            count=0
            while count < k:
                temp = temp.next
                if temp.data not in dp:
                    count += 1
            dp.add(temp.data)
        for i in range(1,n+1):
            if i not in dp:
                return i
        

            