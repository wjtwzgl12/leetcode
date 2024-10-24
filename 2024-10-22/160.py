class Solution:
    def getIntersectionNode(self, headA, headB):
        visited = set() 

        currentA = headA
        while currentA:
            visited.add(currentA)
            currentA = currentA.next

        currentB = headB
        while currentB:
            if currentB in visited:
                return currentB
            currentB = currentB.next
        
        return None
