#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
   
   protected: 
   map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function

};

class LRUCache: public Cache {
    public:
        LRUCache(int i){
            cp = i;
            tail = NULL;
            head = NULL;
        }
        void set(int key, int val) {
            if (head == NULL) {
                Node* newnode = new Node(key, val);
                head = newnode;
                tail = head;
                mp.insert( pair<int, Node*> (key, head));
                return;
            }
            auto it = mp.find(key);
            if ( it != mp.end()) {    // found the key  
                Node* node = it->second;
                node->value = val;
                if (node == head) return; // head
                node->prev->next = node->next;
                if (node == tail) { // tail
                    tail = tail->prev;
                } else {  // in between
                    node->next->prev = node->prev;
                }
                node->next = head;
                node->prev = NULL;
                head->prev = node;
                head = node;
            } else {
                Node* newnode = new Node(head->prev, head, key, val);
                head->prev = newnode;
                head = newnode;
                mp[key] = newnode;
                if (mp.size() > cp) {
                    tail = tail->prev;
                    mp.erase(tail->next->key);
                    delete tail->next;
                    tail->next = NULL;
                }
            }
        }
        int get(int key) {
            if (head == NULL) {
                return (-1);
            }
            if (mp.find(key) != mp.end()) {
                return (mp[key]->value);
            } else {
                return -1;
            }
        }
};

int main() {
   int n, capacity,i;
   cin >> n >> capacity;
   LRUCache l(capacity);
   for(i=0;i<n;i++) {
      string command;
      cin >> command;
      if(command == "get") {
         int key;
         cin >> key;
         cout << l.get(key) << endl;
      } 
      else if(command == "set") {
         int key, value;
         cin >> key >> value;
         l.set(key,value);
      }
   }
   return 0;
}



/* input

8 4
set 4 2
set 2 7
get 2
set 1 8
set 5 9
set 6 15
get 4
get 5
*/
