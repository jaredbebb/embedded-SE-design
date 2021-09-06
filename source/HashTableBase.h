template< typename K, typename V  >
class HashTableBase
{
public:
	virtual V operator[](K key);
	virtual V hashfunction(K key)=0;
};

template< typename K, typename V >
V HashTableBase< K, V >::operator[](K key)
{
	return hashfunction(key);
}


