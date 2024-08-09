class Node :
    
    def __init__(self ,data) :

        self.data =data
        self.next =None

def insertAtBegin(self, data):
    new_node = Node(data)
    if self.head is None:

        self.head = new_node
        return
    
    else:
        new_node.next = self.head
        self.head = new_node
 
def insertAtIndex (self , data , index) :

    if index ==0 :
        insertAtBegin()

    position =0
    current_node = self.head    
        
    while current_node !=None and position != position+1 :

        position = position +1
        current_node = current_node.next

    if current_node !=0 :
        
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
    
    else :
        print ("Not present !")


