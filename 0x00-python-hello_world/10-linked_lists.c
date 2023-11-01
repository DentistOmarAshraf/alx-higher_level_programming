#include "lists.h"

/**
 * print_listint - print linked list
 * @head: pointer of head of linked list
 * Return: number of elements of linked list
 */
size_t print_listint(const listint_t *head)
{
	const listint_t *cur;
	size_t count = 0;

	cur = head;
	while (cur)
	{
		printf("%d\n", cur->n);
		cur = cur->next;
		count++;
	}
	return (count);
}

/**
 * add_nodeint - adding node for linked list
 * @h: pointer of head of linked list
 * @n: the element of new node
 * Return: new node
 */
listint_t *add_nodeint(listint_t **h, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = n;
	new->next = *h;
	*h = new;
	return (new);
}
/**
 * free_listint - free all malloced listint_t nodes
 * @h: pointer of head of linked list
 * Return: NONE
 */
void free_listint(listint_t *h)
{
	if (h)
	{
		free_listint(h->next);
		free(h);
	}
}
