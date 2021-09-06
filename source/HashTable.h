template< typename T = int >
class HashTableBase
{
public:
	// HashTable operator+(const HashTable& p1, const HashTable& p2);
	virtual int operator[](T key);
	virtual int hashfunction(T key)=0;

};

template< typename T >
int HashTableBase<T>::operator[](T key)
{
	return hashfunction(key);
}

template< typename T = int >
class IntHashTable: public HashTableBase<T>
{
public:
	virtual T hashfunction(T key);
};

// CLRS p.263. The division method
template< typename T >
T IntHashTable<T>::hashfunction(T key)
{
	return key % 701;
}

