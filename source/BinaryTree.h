
template< typename K >
class BinaryTree
{
public:

	BinaryTree * left_;
	BinaryTree * right_;
	BinaryTree * p_;
	K key_;

	BinaryTree(K key);
	void insert(BinaryTree * z); // CLRS p.294
	K search(K x, K k); // CLRS p. 290
	void inOrderTreeWalk(K root); // CLRS p. 287

	BinaryTree * left();
	BinaryTree * right();
	K p();
	K key();

};

template< typename K  >
BinaryTree<K>::BinaryTree(K key) :
	left_(nullptr),
	right_(nullptr),
	p_(nullptr),
	key_(key)
{
}


template< typename K  >
void BinaryTree<K>::insert(BinaryTree * z)
{
	BinaryTree<K> * y = nullptr;
	BinaryTree<K> * x = this;
	while (x != nullptr)
	{
		y = x;
		if ( z->key() < x->key() )
		{
			x =  ( x->left_ );
		}
		else
		{
			x = ( x->right_ );
		}
	}
	z->p_ = y;
	if (y == nullptr)
	{
		// root = z
	}
	else if ( z->key() < y->key() )
	{
		y->left_ = z;
	}
	else
	{
		y->right_ = z;
	}
}

template< typename K  >
K BinaryTree<K>::search(K x, K k)
{
}

template< typename K  >
void BinaryTree<K>::inOrderTreeWalk(K root)
{
}

template< typename K  >
BinaryTree<K> * BinaryTree<K>::left()
{
	return left_;
}

template< typename K  >
BinaryTree<K> * BinaryTree<K>::right()
{
	return right_;
}

template< typename K  >
K BinaryTree<K>::p()
{
	return p_->key();
}

template< typename K  >
K BinaryTree<K>::key()
{
	return key_;
}