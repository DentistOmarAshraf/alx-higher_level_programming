#include "lists.h"

/**
 * check_cycle - check if the tail of link list point to head
 * @head: pointer of head of linked list
 * Return: 1 if there is a cyc 0 if not
 */
int check_cycle(listint_t *head)
{
	listint_t *the_head;
	listint_t *cur;

	the_head = head;
	cur = head;
	while (cur)
	{
		cur = cur->next;
		if (!cur)
			return (0);
		if (cur == the_head)
			return (1);
	}
	return (0);
}
