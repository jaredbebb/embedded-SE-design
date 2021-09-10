#include "DynamicSet.h"

template< typename K  >
class Queue: public DynamicSet<K>
{
public:
	virtual void Insert(K element); // Enqueue
	virtual K Delete(); // Dequeue
	Queue();

	size_t  head;
	size_t  tail;
};

template< typename K  >
Queue<K>::Queue():
	DynamicSet<K>::DynamicSet(),
	head(0),
	tail(1)
{
}

template< typename K  >
void Queue<K>::Insert(K element) 
{
	D[tail] = element;
	if (tail == length())
	{
		tail = 1;
	}
	else
	{
		head =+ 1;
	}
}

template< typename K  >
K Queue<K>::Delete()
{
	K k;
	return k;
}