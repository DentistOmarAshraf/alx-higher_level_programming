#include "lists.h"

/**
 * check_cycle - check if the tail of link list point to head
 * @head: pointer of head of linked list
 * Return: 1 if there is a cyc 0 if not
 */
int check_cycle(listint_t *head)
{
	listint_t *the_head;

	the_head = head;
	while (head)
	{
		head = head->next;
		if (head == the_head)
			return (1);
	}
	return (0);
}
