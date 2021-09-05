// amazon-embedded-SE-interview-prep.cpp : Defines the entry point for the application.
//

#include "main.h"

#include "algs_structs/IntElement.h"
#include "algs_structs/IntElement.h"
#include "algs_structs/LinkedList.h"
#include "algs_structs/Util.h"

using namespace std;

int main()
{
	IntElement * h = new IntElement;
	IntElement * t = new IntElement;
	IntElement * n = new IntElement;

	h->prev_ = 0;
	h->key = 9;
	h->next_ = n;

	n->prev_ = h;
	n->key = 5;
	n->next_ = t;

	t->prev_ = n;
	t->key = 16;
	t->next_ = 0;




	IntElement * x = nullptr;
	LinkedList L;
	L.head = h;
	L.tail = t;

	x = List_Search(L, 9);
	std::cout << x->key << "\n";

	x = List_Search(L, 5);
	std::cout << x->key << "\n";

	x = List_Search(L, 16);
	std::cout << x->key << "\n";

	// No Item in list
	x = List_Search(L, 777);
	std::cout << x->key << "\n";


	return 0;
}
