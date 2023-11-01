#include "lists.h"

/**
 * check_cycle - check if the tail of link list point to head
 * @head: pointer of head of linked list
 * Return: 1 if there is a cyc 0 if not
 */
int check_cycle(listint_t *head)
{
	listint_t *ptr1 = head;
	listint_t *ptr2 = head;


	while (ptr1 && ptr2)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
			return (1);
	}
	return (0);
}
