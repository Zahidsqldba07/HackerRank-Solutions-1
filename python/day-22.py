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

    def getHeight(self,root):
        height = 0
        if root != None:
            height_left = 1 + self.getHeight(root.left) if root.left != None else 0
            height_right = 1 + self.getHeight(root.right) if root.right != None else 0
            return height_left if height_left > height_right else height_right
        return height

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       