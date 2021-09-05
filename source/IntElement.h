#pragma once
#include "Element.h"
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

