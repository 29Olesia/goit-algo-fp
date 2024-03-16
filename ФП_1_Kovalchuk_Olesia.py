class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value  
        self.next = next   

def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev  
        prev = current
        current = next_node
    
    return prev

def insertion_sort_linked_list(head):
    dummy = ListNode(0)
    dummy.next = head
    prev_sorted = dummy.next
    current = prev_sorted.next
    
    while current:
        if current.value <= prev_sorted.value:  
            prev_node = dummy
            while prev_node.next and prev_node.next.value < current.value:
                prev_node = prev_node.next
            
            prev_sorted.next = current.next
            current.next = prev_node.next
            prev_node.next = current
            
            current = prev_sorted.next
        else:
            prev_sorted = prev_sorted.next
            current = current.next
    
    return dummy.next

def merge_sorted_lists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        
        current = current.next
    
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    return dummy.next


head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(4)

reversed_head = reverse_linked_list(head)
print("Реверсований список:")
while reversed_head:
    print(reversed_head.value, end=" -> ")
    reversed_head = reversed_head.next
print("None")

sorted_head = insertion_sort_linked_list(head)
print("\nВідсортований список за допомогою сортування вставками:")
while sorted_head:
    print(sorted_head.value, end=" -> ")
    sorted_head = sorted_head.next
print("None")

list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)

merged_head = merge_sorted_lists(list1, list2)
print("\nОб'єднаний відсортований список:")
while merged_head:
    print(merged_head.value, end=" -> ")
    merged_head = merged_head.next
print("None")
