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
	HashTableDivisionMethod<int, int> p1;

	assert(5 == p1[5]);
	assert(3 == p1[704]);

	HashTableDivisionMethod<std::string, int > p2;
	std::string s1 = "key";
	assert(329 == p2.hashfunction(s1));

	return 0;
}


int Test_List()
{

	{
		LinkedList L;
		IntElement * h = new IntElement;
		IntElement * t = new IntElement;
		IntElement * n = new IntElement;

		h->prev_ = 0;
		h->key = 9;
		h->next_ = n;

		n->prev_ = h;
		n->key = 5;
		n->next_ = t;

		t->prev_ = n;
		t->key = 16;
		t->next_ = 0;


		IntElement * x = nullptr;
		
		L.head = h;
		L.tail = t;

		// List Search
		x = List_Search(L, 9);
		assert(9 == x->key);
		std::cout << x->key << "\n";

		x = List_Search(L, 5);
		assert(5 == x->key);
		std::cout << x->key << "\n";

		x = List_Search(L, 16);
		assert(16 == x->key);
		std::cout << x->key << "\n";

		// No Item in list
		x = List_Search(L, 777);
		assert(16 == x->key);
	}
	
	{
		LinkedList L;
		IntElement * h = new IntElement;
		IntElement * t = new IntElement;
		IntElement * n = new IntElement;

		h->prev_ = 0;
		h->key = 9;
		h->next_ = n;

		n->prev_ = h;
		n->key = 5;
		n->next_ = t;

		t->prev_ = n;
		t->key = 16;
		t->next_ = 0;

		IntElement * x = new IntElement;

		L.head = h;
		L.tail = t;

		// List_Insert(LinkedList L, IntElement * x)
		List_Insert(L, x);
		assert(x == L.head);
		assert(h == x->next_);
		assert(nullptr == x->prev_);
	}

	return 0;
}
