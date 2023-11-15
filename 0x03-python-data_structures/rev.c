#include "lists.h"

void rev(listint_t **h)
{
	listint_t *temp;
	listint_t *ptr1;
	listint_t *ptr2;

	temp = NULL;
	ptr1 = *h;
	ptr2 = (*h)->next;

	while (ptr2)
	{
		ptr1->next = temp;
		temp = ptr1;
		ptr1 = ptr2;
		if (!ptr2->next)
		{
			*h = ptr2;
			ptr2->next = temp;
			return;
		}
		ptr2 = ptr2->next;
	}
}
