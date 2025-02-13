class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.start_node = None

    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")

    def InsertToEnd(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def DeleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None

    def delete_at_end(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")

NewDoublyLinkedList = doublyLinkedList()
NewDoublyLinkedList.InsertToEmptyList(input('enter value to empty list : '))
NewDoublyLinkedList.InsertToEnd(input('enter value to end : '))
NewDoublyLinkedList.InsertToEnd(input('enter value to end : '))
NewDoublyLinkedList.InsertToEnd(input('enter value to end : '))
NewDoublyLinkedList.InsertToEnd(input('enter value to end : '))
NewDoublyLinkedList.InsertToEnd(input('enter value to end : '))
NewDoublyLinkedList.Display()
NewDoublyLinkedList.DeleteAtStart()
NewDoublyLinkedList.DeleteAtStart()

print("\n DoublyLinked list after removing a node:")
NewDoublyLinkedList.Display()


































            
                             
               
    
