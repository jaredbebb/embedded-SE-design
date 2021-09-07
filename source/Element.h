#pragma once
template< typename K  >
class Element
{
public:
	Element * prev_;
	Element * next_;
	K key;

	Element();
	virtual ~Element();
};

template< typename K  >
Element<K>::Element() :
	prev_(nullptr),
	next_(nullptr)
{
}

template< typename K  >
Element<K>::~Element()
{
}



