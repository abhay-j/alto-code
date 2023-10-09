def findClosestValueInBst(tree, target):
    # time,space : avg: O(log(n)), O(1) |worst: O(n),O(1)
    closest = float("inf")
    currentNode = tree

    while currentNode is not None:
        
        if abs(closest - target) > abs(currentNode.value - target):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else : 
            break
        

    
    return closest





class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
