#include "lists.h"
/**
 * print_listint - printing linked list item
 * @head: pointer of head of linked list
 * Return: size_t
 */
size_t print_listint(const listint_t *head)
{
	int count = 0;
	const listint_t *ptr = head;

	while (ptr)
	{
		printf("%d\n", ptr->n);
		ptr = ptr->next;
		count++;
	}
	return (count);
}
/**
 * add_nodeint_end - adding node to the tail of linked list
 * @head: pointer of head of linked list
 * @n: int
 * Return: new node
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *ptr;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = n;
	new->next = NULL;
	if (!*head)
	{
		*head = new;
		return (new);
	}
	ptr = *head;
	while (ptr->next)
		ptr = ptr->next;
	ptr->next = new;
	return (new);
}
/**
 * free_listint - free list
 * @head: pointer of head of linked list
 * Return: NONE
 */
void free_listint(listint_t *head)
{
	if (head)
	{
		free_listint(head->next);
		free(head);
	}
}
