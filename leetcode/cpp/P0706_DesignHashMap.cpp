// https://leetcode.com/problems/design-hashmap/
#include <iostream>

struct HashNode {
  int value;
  HashNode* nodes[10];

  HashNode() {
    value = -1;
    for (int ii = 0; ii < 10; ++ii) {
      nodes[ii] = nullptr;
    }
  }
};

class MyHashMap {
 public:
  /** Initialize your data structure here. */
  MyHashMap() { head_ = new HashNode(); }

  /** value will always be non-negative. */
  void put(int key, int value) {
    int key_ = key;

    HashNode* hh = head_;
    int digit = key_ % 10;
    while (key_ > 0) {
      digit = key_ % 10;
      key_ /= 10;
      if (hh->nodes[digit] == nullptr) {
        hh->nodes[digit] = new HashNode();
      }
      hh = hh->nodes[digit];
    }
    hh->value = value;
  }

  /** Returns the value to which the specified key is mapped, or -1 if this map
   * contains no mapping for the key */
  int get(int key) {
    int key_ = key;
    HashNode* hh = head_;
    while (key_ > 0) {
      int digit = key_ % 10;
      key_ /= 10;
      if (hh->nodes[digit] == nullptr) {
        hh->nodes[digit] = new HashNode();
      }
      hh = hh->nodes[digit];
    }
    return hh->value;
  }

  /** Removes the mapping of the specified value key if this map contains a
   * mapping for the key */
  void remove(int key) {
    int key_ = key;
    HashNode* hh = head_;
    int digit = key_ % 10;
    while (key_ > 0) {
      digit = key_ % 10;
      key_ /= 10;
      if (hh->nodes[digit] == nullptr) {
        hh->nodes[digit] = new HashNode();
      }
      hh = hh->nodes[digit];
    }
    hh->value = -1;
  }

 private:
  HashNode* head_;
};

int main(int argc, char** argv) {
  MyHashMap* obj = new MyHashMap();
  obj->put(3, 4);
  int param_2 = obj->get(3);
  obj->remove(2);
  std::cout << param_2 << std::endl;
}