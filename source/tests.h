#include "Element.h"
#include "LinkedList.h"
#include "HashTableDivisionMethod.h"
#include "Queue.h"
#include "Stack.h"
#include "BinaryTree.h"

#include <string>

#define DEBUG

#include <assert.h>     /* assert */
#include <iostream>

using namespace std;

int Test_Tree()
{
	// insert
	{

		BinaryTree<int> root(2);
		BinaryTree<int> * left = new BinaryTree<int>(1);
		BinaryTree<int> * right = new BinaryTree<int>(3);

		BinaryTree<int> * leftleft = new BinaryTree<int>(1);
		BinaryTree<int> * leftright = new BinaryTree<int>(1);

		root.insert(left);
		root.insert(right);
		root.insert(leftleft);
		root.insert(leftright);

		assert(root.left() == left);
		assert(root.right() == right);
		assert(root.left()->key() == 1);
		assert(root.right()->key() == 3);

		assert(left->right()->key() == 1);
		assert( left->left() == nullptr);

		assert(BinaryTree<int>::count() == 5);
	}
	// ensure memory is cleaned up responsibly
	{
		
		assert(BinaryTree<int>::count() == 0);
	}
	// insert, root is on heap
	{
		BinaryTree<int> * root = new BinaryTree<int>(2);
		BinaryTree<int> * left;
		BinaryTree<int> * right;
		{
			left = new BinaryTree<int>(1);
			right = new BinaryTree<int>(3);
			root->insert(left);
			root->insert(right);
		}

		delete root;
		root = 0;

		// ensure memory is cleaned up responsibly
		assert(BinaryTree<int>::count() == 0);
	}


	// delete
	{

	}

	// search
	{

	}

	return 0;
}


int Test_Stack()
{
	// push
	{
		Stack<int> s;
		for (size_t i = 10; i < 18;  i++) {
			s.Insert(i);
		}
		assert(s.top() == 4);
	}
	// pop
	{
		Stack<int> s;
		for (size_t i = 10; i < 18;  i++) {
			s.Insert(i);
		}
		assert(s.Delete() == 17);
	}
	// pop underflow
	{
		Stack<int> s;
		bool does_throw = false;
		try {
			assert(s.Delete() == 17);
		}
		catch (std::underflow_error) {
			does_throw = true;
		}
		assert(does_throw);
	}
	return 0;
}

int Test_Queue() 
{
	// Enqueue
	{
		Queue<int> q;
		for (size_t i = 10; i < 18; i++) {
			q.Insert(i);
		}
	}
	// Dequeue
	{
		Queue<int> q;
		for (size_t i = 1; i < 4; i++)
		{
			q.Insert(i);
		}
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
