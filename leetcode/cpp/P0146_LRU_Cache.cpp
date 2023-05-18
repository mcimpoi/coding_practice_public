/* https://leetcode.com/problems/lru-cache */
#include <iostream>
#include <list>
#include <unordered_map>
#include <utility>

using namespace std;

class LRUCache {
 public:
  LRUCache(int capacity) { m_capacity = capacity; }

  int get(int key) {
    auto search_result = hash.find(key);
    if (search_result != hash.end()) {
      auto list_it = search_result->second;
      int key = list_it->first;
      int value = list_it->second;
      cache.erase(list_it);
      cache.push_front(make_pair(key, value));
      hash[key] = cache.begin();
      return value;
    } else {
      return -1;
    }
  }

  void put(int key, int value) {
    auto search_result = hash.find(key);
    if (search_result != hash.end()) {
      auto list_it = search_result->second;
      int key = list_it->first;
      cache.erase(list_it);
    } else {
      if (cache.size() == m_capacity) {
        pair<int, int> back = cache.back();
        hash.erase(back.first);
        cache.pop_back();
      }
    }
    cache.push_front(make_pair(key, value));
    hash[key] = cache.begin();
  }

 private:
  int m_capacity;
  list<pair<int, int>> cache;
  unordered_map<int, list<pair<int, int>>::iterator> hash;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

int main(int argc, char **argv) {
  LRUCache obj(2);
  int res = obj.get(1);
  cout << res << "\n";
  obj.get(2);
  obj.put(2, 6);
  obj.get(1);
  res = obj.get(1);
  cout << res << "\n";
  obj.put(3, 3);
  res = obj.get(1);
  cout << res << "\n";
  return 0;
}
