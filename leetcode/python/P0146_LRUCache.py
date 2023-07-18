# https://leetcode.com/problems/lru-cache/

from typing import Optional
import ast


class ListNode:
    def __init__(self, key: int, value: int):
        self._next: Optional["ListNode"] = None
        self._prev: Optional["ListNode"] = None
        self.key = key
        self.val = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_val: Optional["ListNode"]):
        self._next = next_val

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_val: Optional["ListNode"]):
        self._prev = prev_val

    def __str__(self) -> str:
        return (
            f"k: {self.key} v:{self.val}"
            f"prev: {self._prev.key if self._prev is not None else 'None'}"
            f"next {self._next.key if self._next is not None else 'None'}"
        )


class LRUCache:
    # get and put in O(1)
    #  --> hint to use a hashmap
    #  need to discard the least recently used
    # ==> every time a key is accessed => move to the front of a list
    # if we use singly linked list, we need previous element when
    # we update the list on access --> use doubly linked list
    def move_to_head_(self, key: int):
        crt_node = self.keys[key]
        if crt_node.prev is None:
            return
        crt_node.prev.next = crt_node.next
        if crt_node.next is not None:
            crt_node.next.prev = crt_node.prev
        else:
            self.tail = crt_node.prev
        crt_node.next = self.head
        self.head.prev = crt_node
        crt_node.prev = None
        self.head = crt_node

    def __init__(self, capacity: int):
        self.capacity = 0
        self.max_capacity = capacity
        self.keys = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        # print(f"Get: {key}")
        if key in self.keys:
            ret_val = self.keys[key].val
            # print(f" get:: head before: {self.head}")
            self.move_to_head_(key)
            # print(f" get:: head after: {self.head}")
            return ret_val
        else:
            # print(" get: -1")
            return -1

    def put(self, key: int, value: int) -> None:
        # print(f"Put {key} {value} before put: head: {self.head} tail: {self.tail}")
        if key in self.keys:
            self.keys[key].val = value
            self.move_to_head_(key)
        else:
            if self.capacity >= self.max_capacity:
                new_tail = self.tail.prev
                prev_tail_key = self.tail.key

                if new_tail is not None:
                    self.tail.prev.next = None
                    self.tail.prev = None
                    new_tail.next = None
                    self.tail = new_tail
                else:
                    self.tail = None
                    if self.max_capacity == 1:
                        self.head = None

                self.keys.pop(prev_tail_key)
                self.capacity -= 1

            new_head = ListNode(key, value)
            self.keys[key] = new_head
            if self.head is None and self.tail is None:
                self.head = new_head
                self.tail = new_head
                # print("H: ", self.head, "T: ", self.tail, "Cap:", self.capacity)
            else:
                new_head.next = self.head
                self.head.prev = new_head
                self.head = new_head
            self.capacity += 1


if __name__ == "__main__":
    with open("examples/P0146.txt", "r") as f:
        lines = f.readlines()

    for l1, l2 in zip(lines[0::2], lines[1::2]):
        cmds = ast.literal_eval(l1)
        params = ast.literal_eval(l2)
        cache = None
        res = []
        for cmd, param in zip(cmds, params):
            if cmd == "LRUCache":
                cache = LRUCache(*param)
                res.append(None)
            elif cmd == "put":
                res.append(cache.put(*param))
            elif cmd == "get":
                res.append(cache.get(*param))
            else:
                raise ValueError(f"Invalid param {cmd}")
        print(res)
