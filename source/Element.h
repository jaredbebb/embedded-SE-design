#pragma once
class Element
{

// TODO make Element Template class
public:
	Element();
	virtual ~Element();

	Element * prev_;
	Element * next_;
	int key;
};


