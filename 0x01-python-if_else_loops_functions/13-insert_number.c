#include "lists.h"
/**
 * insert_node - inserting node in sorted linked list
 * @head: pointer of pointer
 * @number: int
 * Return: new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *ptr;
	listint_t *ptr2;

	ptr = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (new->n < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (new->n > ptr->next->n)
	{
		ptr = ptr->next;
		if (!(ptr->next))
		{
			ptr->next = new;
			new->next = NULL;
			return (new);
		}
	}
	ptr2 = ptr->next;
	ptr->next = new;
	new->next = ptr2;
	return (new);
}
