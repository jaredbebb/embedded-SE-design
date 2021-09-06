#include "LinkedList.h"

template< typename K, typename V  >
class HashTableBase
{
public:
	
	const int m = 701; // number of slots
	HashTableBase();

	virtual V operator[](K key); // get value
	virtual void insert(K key, V value); // set/update value
	LinkedList * T; // array representing hash table slots
	virtual V hashfunction(K key)=0;

	
};


template< class K, typename V >
HashTableBase< K, V >::HashTableBase() :
	T(new LinkedList[m])
{
}

template< typename K, typename V >
void HashTableBase< K, V >::insert(K key, V value)
{
	V index = hashfunction(key);
	IntElement * temp = new IntElement;
	temp->key = value;
	List_Insert(T[index], temp);
}

template< typename K, typename V >
V HashTableBase< K, V >::operator[](K key)
{
	return hashfunction(key);
}


