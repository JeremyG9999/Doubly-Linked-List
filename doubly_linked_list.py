class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  
        self.prev = None  #reverse
class DoublyLinkedList:
    def __init__(self):  
        self.head = None
    def printList(self):    
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def push(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head.prev = newnode  #reverse
        self.head = newnode
    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp   #reverse
        return newnode
    def insertAfter(self, prevnode, data):
        if prevnode is None:
            pass
        else:
            newnode = Node(data)
            newnode.next = prevnode.next
            prevnode.next = newnode
            newnode.prev = prevnode #reverse
        if newnode.next:    #reverse
            newnode.next.prev = newnode  #reverse
    def printListReversed(self):   #reverse
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        while temp:
            print(temp.data)
            temp = temp.prev
def main():
    doublylist = DoublyLinkedList()
    doublylist.append(3)
    doublylist.append(4)
    doublylist.append(5)
    doublylist.push(8)
    doublylist.insertAfter(doublylist.head.next, "6")
    print("Linked List:")
    doublylist.printList()
    print("Doubly Linked List:")
    doublylist.printListReversed()
main()