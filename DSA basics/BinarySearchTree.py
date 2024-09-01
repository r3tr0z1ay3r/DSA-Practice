class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert
# a new node with the given key

class BST():
    def __init__(self,root) -> None:
         self.root = root

    def insert(self, key):
        newNode = Node(key)
        parent = None
        curr = self.root
        while curr is not None:
            parent = curr
            if curr.val > key:
                curr = curr.left
            elif curr.val < key:
                curr = curr.right
            else:
                raise Exception("val already present in tree")
        if parent.val > key:
            parent.left = newNode
            print("The value {} is appened to the  left of {}".format(newNode.val,parent.val))
        else:
            parent.right = newNode
            print("The value {} is appened to the  right of {}".format(newNode.val,parent.val))

    def getMinVal(self,node):
        currentNode = node
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.val

    def delNode(self,val,parent=None):
        currentNode = self.root
        while currentNode is not None:
            if val < currentNode.val:
                parentNode = currentNode
                currentNode = currentNode.left  
            elif val > currentNode.val:
                parentNode = currentNode
                currentNode = currentNode.right
            #Found the node
            else:   
            #two child ondes
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.val = self.getMinVal(currentNode.right)     #get the left number from the right subtree)
                    currentNode.right = self.delNode(currentNode.val, currentNode.right) #remove that most left number by using remove() 
                                                                             #on the right currentNode
                #root node
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.val = currentNode.left.val
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.val = currentNode.right.val
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    #only 1 item left in BST
                    else:
                        pass
                #one child node
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self
    def isPresent(self,val):
        curr = self.root
        while curr is not None:
            if val > curr.val:
                curr = curr.right
            elif val < curr.val:
                curr = curr.left
            else:
                print("Value found in Tree")
                return True
        print("Value not in Tree")
        return False

    def inorder_stack(self):
        traversal = []
        node = self.root
        stack = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                traversal.append(node.val)
                node = node.right
                
        return traversal


obj = BST(Node(50))

obj.insert(30)
obj.insert(20)
obj.insert(40)
obj.insert(70)
obj.insert(60)
obj.insert(80)

obj.delNode(30)

print(obj.inorder_stack())