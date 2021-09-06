template< typename K = int, typename V = int  >
class HashTableBase
{
public:
	virtual int operator[](K key);
	virtual int hashfunction(K key)=0;
};

template< typename K, typename V >
int HashTableBase< K, V >::operator[](K key)
{
	return hashfunction(key);
}


