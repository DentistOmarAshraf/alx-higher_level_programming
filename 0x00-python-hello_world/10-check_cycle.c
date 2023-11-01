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

	while (1)
	{
		if (!ptr1)
			return (0);
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1->next == NULL || ptr2->next->next == NULL)
			return (0);
		if (ptr1->next == ptr2->next->next)
			return (1);
	}
}
