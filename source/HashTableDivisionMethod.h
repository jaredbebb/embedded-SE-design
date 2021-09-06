#include "HashTableBase.h"

template< typename K = int, typename V = int  >
class HashTableDivisionMethod : public HashTableBase<K>
{
public:
	virtual K hashfunction(K key);
};

// CLRS p.263. The division method
template< typename K, typename V >
K HashTableDivisionMethod< K, V >::hashfunction(K key)
{
	return key % 701;
}
