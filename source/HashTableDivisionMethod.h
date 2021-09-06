#include "HashTableBase.h"
#include <string>
#include <numeric>

using namespace std;

template< class K, typename V  >
class HashTableDivisionMethod : public HashTableBase<K,V>
{
public:
	
	virtual V hashfunction(K key);
	HashTableDivisionMethod();
};

template< class K, typename V >
HashTableDivisionMethod< K, V >::HashTableDivisionMethod(): 
	HashTableBase()
{
}

// CLRS p.263. The division method
template< class K, typename V >
V HashTableDivisionMethod< K, V >::hashfunction(K key)
{
	return key % m;
}

int HashTableDivisionMethod< std::string, int >::hashfunction(std::string key)
{
	return std::accumulate(key.begin(), key.end(), 0) % m;
}
