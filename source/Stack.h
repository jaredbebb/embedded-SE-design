#pragma once
#include "DynamicSet.h"

template< typename K  >
class Stack : public DynamicSet<K>
{
public:
	virtual void Insert(K element); // Push
	virtual K Delete();  // Pop
	Stack();
	bool Empty();
	size_t top();
private:
	size_t top_;
};

template< typename K  >
Stack<K>::Stack() :
	DynamicSet<K>::DynamicSet(),
	top_(0)
{
}

template< typename K  >
void Stack<K>::Insert(K element)
{
	D[top()] = element;
	if (top() == length()-1)
	{
		return;
	}
	top_ += 1;
}

template< typename K  >
K Stack<K>::Delete()
{
	if ( Empty() )
	{
		throw std::underflow_error("Stack is empty");
	}
	else
	{
		top_ -= 1;
		return D[top() + 1];
	}
}

template< typename K  >
bool Stack<K>::Empty()
{
	return top() == 0;
}

template< typename K  >
size_t Stack<K>::top()
{
	return top_;
}