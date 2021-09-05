#pragma once

#include "IntElement.h"

#include "LinkedList.h"

// Searching a linked list CLRS p.237 
IntElement * List_Search(LinkedList L, int k)
{
	IntElement * x = L.head;
	// 0 is null
	while (x->next_ != nullptr && x->key != k)
	{
		x = x->next_;
	}
	return x;
}