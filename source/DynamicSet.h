template< typename K  >
class DynamicSet
{
public:
	virtual void Insert(K element)=0;
	virtual K Delete()=0;
};