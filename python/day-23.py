import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def height(self, node):
        if node is None:
            return 0
        else :
            lheight = self.height(node.left)
            rheight = self.height(node.right)

        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1
        
    def levelOrder(self,root):
        h = self.height(root)
        for i in range(h+1):
            self.printLevel(root, i)

    def printLevel(self,root,level):
        if root is None:
            return
        if level == 1:
            print(root.data,end=" ")
        elif level > 1 :
            self.printLevel(root.left , level-1)
            self.printLevel(root.right , level-1)        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
