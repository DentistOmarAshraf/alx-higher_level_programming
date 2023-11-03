#include "lists.h"

/**
 * print_listint - print (n) of linked list
 * @h: head of linked list
 * Return: number of elements
 */
size_t print_listint(const listint_t *h)
{
	size_t count = 0;
	const listint_t *ptr;

	ptr = h;
	while (ptr)
	{
		printf("%d\n", ptr->n);
		ptr = ptr->next;
		count++;
	}
	return (count);
}

/**
 * add_nodeint_end - adding node object at the end of linked list
 * @head: pointer of pointer of head of linked list
 * @n: int
 * Return: new node
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *ptr;

	ptr = *head;
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
	while (ptr->next)
		ptr = ptr->next;
	ptr->next = new;
	return (new);
}

/**
 * free_listint - free malloced node
 * @head: head of linked list
 * Return: Void NONE
 */
void free_listint(listint_t *head)
{
	if (head)
	{
		free_listint(head->next);
		free(head);
	}
}
