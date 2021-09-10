template< typename K  >
class Stack
{
public:
	virtual void Insert(K element) = 0; // Push
	virtual K Delete() = 0;  // Pop
	virtual Stack();
	virtual ~Stack();
};