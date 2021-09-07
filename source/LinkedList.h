#pragma once

#include "IntElement.h"

template< typename K  >
class LinkedList
{
public:
	LinkedList();
	~LinkedList();

	IntElement<int> * head;
	IntElement<int> * tail;

	K * search(int k);
	void insert(K * x);

private:

};

// Searching a linked list CLRS p.237
template< typename K  >
K * LinkedList<K>::search(int k)
//IntElement * List_Search(LinkedList & L, int k)
{
	IntElement<int> * x = head;
	// 0 is null
	while (x->next_ != nullptr && x->key != k)
	{
		x = x->next_;
	}
	return x;
}

template< typename K  >
void LinkedList<K>::insert(K * x)
//void List_Insert(LinkedList & L, IntElement * x)
{
	x->next_ = head;
	if (head != nullptr)
	{
		head->prev_ = x;
	}
	head = x;
	x->prev_ = nullptr;
}

template< typename K  >
LinkedList<K>::LinkedList()
{
	head = new IntElement<int>;
	tail = new IntElement<int>;
}

template< typename K  >
LinkedList<K>::~LinkedList()
{
}