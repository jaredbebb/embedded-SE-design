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
	tail(0)
{
}

template< typename K  >
void Queue<K>::Insert(K element) 
{
	// Overflow condition
	if (tail == n)
	{
		tail = 0;
	}
	D[tail] = element;
	tail += 1;
}

template< typename K  >
K Queue<K>::Delete()
{
	K x = 0;
	if (head == tail)
	{
		return x;
	}
	x = D[head];
	if (head == n)
	{
		head = 0;
	}
	else
	{
		head +=  1;
	}
	return x;
}