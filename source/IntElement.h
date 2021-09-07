#pragma once
#include "Element.h"

template< typename K  >
class IntElement :
	public Element
{
public:
	IntElement();
	virtual ~IntElement();

	IntElement * prev_;
	IntElement * next_;

	int key;
};

template< typename K  >
IntElement<K>::IntElement() :
	prev_(nullptr),
	next_(nullptr)
{
}

template< typename K  >
IntElement<K>::~IntElement()
{
}


