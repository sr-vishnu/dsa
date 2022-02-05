
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def insert(value,treeNode):
    if value == treeNode.value:
        return
    elif(value > treeNode.value):
        if(treeNode.right is None):
            treeNode.right = TreeNode(value)
        else:
            insert(value, treeNode.right)
    else:
        if(treeNode.left is None):
            treeNode.left = TreeNode(value)
        else:
            insert(value, treeNode.left)

def delete(value,treeNode):
    
    if(value > treeNode.value):
        treeNode.right = delete(value, treeNode.right)
    elif(value < treeNode.value):
        treeNode.left = delete(value, treeNode.left)
    else:
        if treeNode.left is None:
            return treeNode.right
        elif treeNode.right is None:
            return treeNode.left
        else:
            successor = findInOrderSuccessor(treeNode.right)
            treeNode.value = successor.value
            treeNode.right = delete(successor.value,treeNode.right)
    return treeNode


def find(value,treeNode):
    if treeNode.value == value:
        return treeNode
    elif((treeNode.right is not None) and value > treeNode.value):
        return find(value, treeNode.right)
    elif((treeNode.left is not None) and value < treeNode.value):
        return find(value, treeNode.left)
    else:
        return None


def inOrderTraversal(aTree):

    result = []
    
    def doInOrderTraversal(theTree):
        if(theTree.left is not None):
            doInOrderTraversal(theTree.left)
        result.append(theTree.value)
        if(theTree.right is not None):
            doInOrderTraversal(theTree.right)

    doInOrderTraversal(aTree)
    return result

def findInOrderSuccessor(aTree):
        if(aTree.left is not None):
            return findInOrderSuccessor(aTree.left)
        return aTree



aTree = TreeNode(1)

insert(2, aTree)
insert(3, aTree)
insert(100,aTree)
insert(99, aTree)


print(aTree.value)
print(aTree.right.value)
print(aTree.right.right.value)
print(aTree.right.right.right.value)
print(aTree.right.right.right.left.value)


print(f"inorder traversal: {inOrderTraversal(aTree)}")

delete(99, aTree)


print(f"inorder traversal: {inOrderTraversal(aTree)}")


anotherTree = TreeNode(50)
insert(30, anotherTree)
insert(60, anotherTree)
insert(55, anotherTree)
insert(100,anotherTree)


print(f"inorder traversal: {inOrderTraversal(anotherTree)}")

delete(60, anotherTree)

print(f"inorder traversal: {inOrderTraversal(anotherTree)}")
