class Tree :
    def __init__(self , value ) :
        self.value = value
        if self.value :
            self.left = Tree()
            self.right= Tree()
        else :
            self.left = None
            self.right = None
        
    def isempty(self) :
        return self.value==None
    
    def insert (self, data) :

        if self.isempty() :

            self.value = data
            self.left = Tree()
            self.right = Tree ()

            print ("{} Inserted Succesflly 0".format(self.value))
        
        elif data < self.value :
             self.left.insert(data)
             return
        
        elif data > self.value :
             self.right.insert(data)
             return
        
        elif data == self.value :
            return