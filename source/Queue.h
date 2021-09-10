#include "DynamicSet.h"

template< typename K  >
class Queue: public DynamicSet<K>
{
public:
	virtual void Insert(K element); // Enqueue
	virtual K Delete(); // Dequeue
	Queue();
};

template< typename K  >
Queue<K>::Queue() {
}

template< typename K  >
void Queue<K>::Insert(K element) 
{
}

template< typename K  >
K Queue<K>::Delete()
{
	K k;
	return k;
}