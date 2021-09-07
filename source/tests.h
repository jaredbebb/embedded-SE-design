// main.cpp : Defines the entry point for the application.
//



#include "IntElement.h"
#include "IntElement.h"
#include "LinkedList.h"
#include "Util.h"
#include "HashTableDivisionMethod.h"
#include <string>

#define DEBUG

#include <assert.h>     /* assert */
#include <iostream>

using namespace std;

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
		LinkedList <IntElement<int>> L;
		IntElement<int> * h = new IntElement<int>;
		IntElement<int> * t = new IntElement<int>;
		IntElement<int> * n = new IntElement<int>;

		h->prev_ = 0;
		h->key = 9;
		h->next_ = n;

		n->prev_ = h;
		n->key = 5;
		n->next_ = t;

		t->prev_ = n;
		t->key = 16;
		t->next_ = 0;


		IntElement<int> * x = nullptr;
		
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
		LinkedList <IntElement<int>> L;
		IntElement<int> * h = new IntElement<int>;
		IntElement<int> * t = new IntElement<int>;
		IntElement<int> * n = new IntElement<int>;

		h->prev_ = 0;
		h->key = 9;
		h->next_ = n;

		n->prev_ = h;
		n->key = 5;
		n->next_ = t;

		t->prev_ = n;
		t->key = 16;
		t->next_ = 0;

		IntElement<int> * x = new IntElement<int>;

		L.head = h;
		L.tail = t;

		// List_Insert(LinkedList L, IntElement * x)
		L.insert( x);
		assert(x == L.head);
		assert(h == x->next_);
		assert(nullptr == x->prev_);
	}

	return 0;
}
