import sys
from typing import Optional


class Node:

    def __init__(self, val: str):
        self.val: str = val
        self.next: Optional[Node] = None

def create_linked_list(l: list[str]) -> Node:
    head = Node("h")

    cur_node = head
    for val in l:
        cur_node.next = Node(val)
        cur_node = cur_node.next
    return head

def sanitize_zeros(num_str: str) -> str:
    i = 0
    while i < len(num_str) and num_str[i] == "0":
        i+=1
    
    return "0" if i == len(num_str) else num_str[i:]

def simulate(head: Optional[Node], prev: Optional[Node]) -> None:

    cur_node = head
    prev = None

    while cur_node:

        if cur_node.val == "h":
            prev = cur_node
            cur_node = cur_node.next
            continue

        if cur_node.val == "0":
            cur_node.val = "1"
            prev = cur_node
            cur_node = cur_node.next
            continue

        if len(cur_node.val) % 2 == 0:
            # split into two stones
            lnode = Node(cur_node.val[:len(cur_node.val)//2])
            rnode = Node(sanitize_zeros(cur_node.val[len(cur_node.val)//2:]))
        
            temp = cur_node.next
            if prev:
                prev.next = lnode 

            lnode.next = rnode
            rnode.next = temp
            prev = rnode
            cur_node = temp
            continue
        
        cur_node.val = str(int(cur_node.val) * 2024)
        prev = cur_node
        cur_node = cur_node.next



def print_linked_list(head: Optional[Node]) -> None:
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next
    print()

def count_stones(head: Optional[Node]) -> int:
    count = 0
    while head:
        if head.val != "h": 
            count += 1
        head = head.next

    return count

if __name__ == "__main__":
    args = sys.argv[1:]

    file_name = args[0]

    with open(file_name) as file:

        stones = file.readline().strip().split(" ")

        head = create_linked_list(stones)
        print_linked_list(head)

        for i in range(75):
            simulate(head, None)
            # print_linked_list(head)

        print(count_stones(head))


