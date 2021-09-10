#include "Element.h"
#include "LinkedList.h"
#include "HashTableDivisionMethod.h"
#include "Queue.h"

#include <string>

#define DEBUG

#include <assert.h>     /* assert */
#include <iostream>

using namespace std;

int Test_Queue() {
	// Enqueue
	{
		Queue<int> q;
		q.Insert(10);
		q.Insert(11);
		q.Insert(12);
		q.Insert(13);
		q.Insert(14);
		q.Insert(15);
		q.Insert(16);
		q.Insert(17);
	}
	
	// Dequeue
	{
		Queue<int> q;
		q.Insert(1);
		q.Insert(2);
		q.Insert(3);
		int d = q.Delete();
	}
	// Dequeue underflow
	{
		Queue<int> q;
		int d = q.Delete();
	}
	
	return 0;
}


int Test_HashTable() {
	{
		// Test retrieving items
		HashTableDivisionMethod<int, int> p1;

		assert(5 == p1[5]);
		assert(3 == p1[704]);
	}
	{
		// Test retrieving hash
		HashTableDivisionMethod<std::string, int > p1;
		std::string s1 = "key";
		assert(329 == p1.hashfunction(s1));
	}
	{
		// Test inserting new/updating values
		HashTableDivisionMethod<int, int> p1;
		p1.insert(5, 12);
		p1.insert(5, 12);
	}
	return 0;
}


int Test_List()
{
	{
		LinkedList <Element<int>> L;
		Element<int> * h = new Element<int>;
		Element<int> * t = new Element<int>;
		Element<int> * n = new Element<int>;

		h->prev_ = 0;
		h->key = 9;
		h->next_ = n;

		n->prev_ = h;
		n->key = 5;
		n->next_ = t;

		t->prev_ = n;
		t->key = 16;
		t->next_ = 0;


		Element<int> * x = nullptr;
		
		L.head = h;
		L.tail = t;

		// List Search
		x = L.search(9);
		assert(9 == x->key);
		std::cout << x->key << "\n";

		x = L.search(5);
		assert(5 == x->key);
		std::cout << x->key << "\n";

		x = L.search(16);
		assert(16 == x->key);
		std::cout << x->key << "\n";

		// No Item in list
		x = L.search(777);
		assert(16 == x->key);
	}
	{
		LinkedList <Element<int>> L;
		Element<int> * h = new Element<int>;
		Element<int> * t = new Element<int>;
		Element<int> * n = new Element<int>;

		h->prev_ = 0;
		h->key = 9;
		h->next_ = n;

		n->prev_ = h;
		n->key = 5;
		n->next_ = t;

		t->prev_ = n;
		t->key = 16;
		t->next_ = 0;

		Element<int> * x = new Element<int>;

		L.head = h;
		L.tail = t;

		// List_Insert(LinkedList L, Element * x)
		L.insert( x);
		assert(x == L.head);
		assert(h == x->next_);
		assert(nullptr == x->prev_);
	}

	return 0;
}
