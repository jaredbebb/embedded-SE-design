template< typename K  >
class DynamicSet
{
public:
	const int n = 120;
	K * D = nullptr;
	DynamicSet();
	~DynamicSet();
	virtual void Insert(K element) = 0;
	virtual K Delete()=0;

	virtual size_t length();
};

template< typename K  >
DynamicSet<K>::DynamicSet() :
	D(new K[n])
{

}

template< typename K  >
DynamicSet<K>::~DynamicSet() {
	delete [] D;
	D = nullptr;
}

template< typename K  >
size_t DynamicSet<K>::length() {
	return sizeof(D) / sizeof(*D);
}