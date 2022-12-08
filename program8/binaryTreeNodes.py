class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left # set original left child as the left child of newNode
            self.left = t # newNode is the left child

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right