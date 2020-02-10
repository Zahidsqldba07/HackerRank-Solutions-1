# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    current = root

    # v1Anestors = getListOfAncetors(root, v1)
    # v2Anestors = getListOfAncetors(root, v2)

    if root is None:
        return None

    if root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)

    if root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)

    return root

def getListOfAncetors(tree, v):
    if tree == None:
        return []
    elif tree.info == v:
        l = []
        l.append(tree)
        return l
    elif tree.info < v:
        l = []
        l.append(tree)
        l.extend(getListOfAncetors(tree.left, v))
        return l
    else: 
        l = []
        l.append(tree)
        l.extend(getListOfAncetors(tree.right, v))
        return l

