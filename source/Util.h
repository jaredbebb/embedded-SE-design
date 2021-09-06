#pragma once

#include "IntElement.h"

#include "LinkedList.h"

// Searching a linked list CLRS p.237 
IntElement * List_Search(LinkedList & L, int k)
{
	IntElement * x = L.head;
	// 0 is null
	while (x->next_ != nullptr && x->key != k)
	{
		x = x->next_;
	}
	return x;
}

void List_Insert(LinkedList & L, IntElement * x)
{
	x->next_ = L.head;
	if(L.head != nullptr )
	{
		L.head->prev_ = x;
	}
	L.head = x;
	x->prev_ = nullptr;
}