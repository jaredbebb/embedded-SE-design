template< typename K  >
class BinaryTree
{
public:

	K left;
	K right;
	K p;
	K key;

	insert(K T, K z); // CLRS p.294
	search(K x, K k); // CLRS p. 290
	inOrderTreeWalk(K root); // CLRS p. 287

};