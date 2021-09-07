#pragma once

#include "Element.h"

template< typename K  >
class LinkedList
{
public:
	LinkedList();
	~LinkedList();

	Element<int> * head;
	Element<int> * tail;

	K * search(int k);
	void insert(K * x);

private:

};

// Searching a linked list CLRS p.237
template< typename K  >
K * LinkedList<K>::search(int k)
//Element * List_Search(LinkedList & L, int k)
{
	Element<int> * x = head;
	// 0 is null
	while (x->next_ != nullptr && x->key != k)
	{
		x = x->next_;
	}
	return x;
}

template< typename K  >
void LinkedList<K>::insert(K * x)
//void List_Insert(LinkedList & L, Element * x)
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
	head = new Element<int>;
	tail = new Element<int>;
}

template< typename K  >
LinkedList<K>::~LinkedList()
{
}