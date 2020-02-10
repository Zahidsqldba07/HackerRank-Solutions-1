# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    h = 0
    hLeft = 0
    hRight = 0

    if root.left:
        hLeft = getHeight(root.left, 1)
    if root.right:
        hRight = getHeight(root.right, 1)

    if hLeft > hRight:
        h = hLeft
    else:
        h = hRight

    return h

def getHeight(root, level):
    h = 0
    hLeft = 0
    hRight = 0

    if root.left:
        hLeft = getHeight(root.left, level+1)
    if root.right:
        hRight = getHeight(root.right, level+1)

    if not root.left and not root.right:
        h = level
    elif hLeft > hRight:
        h = hLeft
    else:
        h = hRight

    return h

