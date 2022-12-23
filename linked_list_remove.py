class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"<Node|{self.value}>"
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def _get_node(self, value_to_get):
        check = self.head
        while check is not None:
            if check.value == value_to_get:
                return check
            check = check.next
        return None
        
    def push_on(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, new_value):
        new_node = Node(new_value)
        
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node
            
    def insert_after(self, prev_value, new_value):
        prev_node = self._get_node(prev_value)
        if prev_node is None:
            print(f"{prev_value} is not in linked list")
            return
        
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def traverse_list(self):
        node = self.head
        while node:
            print(node) 
            node = node.next
    
    def remove(self, value_to_remove):
        to_remove = self._get_node(value_to_remove)
        zero_index = self.head
        while zero_index:
            if zero_index.next == to_remove:
                zero_index.next = to_remove.next
                return
    
            zero_index = zero_index.next

        
        # to_remove = to_remove.next 
        # to_remove.next = to_remove.next.next


        # if get_rid_of_position == self.head:


        # if self.next == get_rid_of_position:
        # get_rid_of_position.next = self.next            

# weekdays = LinkedList()
# weekdays.push_on('Wednesday')
# weekdays.push_on('Monday')
# weekdays.append('Thursday')
# weekdays.append('Friday')
# weekdays.insert_after('Monday', 'Tuesday')
# weekdays.traverse_list()

weekdays = LinkedList()
list_of_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for day in list_of_days:

    weekdays.append(day)

weekdays.remove('Wednesday')

    
        # value_to_remove = self._get_node
        # if value_to_remove.prev_node is None:
        #     self.head.remove()
        # elif value_to_remove.next is None:
        #     remove[:-1]
        # else:
        #     value_to_remove = value_to_remove.prev
        # return
weekdays.traverse_list()