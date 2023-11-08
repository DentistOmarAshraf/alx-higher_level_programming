#include "lists.h"
/**
 * listsize - function to know how many nodes in linked list
 * I build this func to help in is_palindrome()
 * @head: pointer of head of linked list
 * Return: int , size of linked list
 */
int listsize(listint_t *head)
{
	int count = 0;

	while (head)
	{
		head = head->next;
		count++;
	}
	return (count);
}

/**
 * is_palindrome - function that know if the l.list is pali
 * @head: pointer of pointer
 * Return: 1 if pali 0 if not
 */

int is_palindrome(listint_t **head)
{
	int size_list, i, x, y, a, b;
	listint_t *ptr = *head;

	if (!*head)
		return (1);
	size_list = listsize(*head);
	for (i = 0 ; i < listsize(*head) / 2 ; i++)
	{
		for (x = 0 ; x < i ; x++)
			ptr = ptr->next;
		a = ptr->n;
		ptr = *head;
		for (y = 0 ; y < size_list - 1 ; y++)
			ptr = ptr->next;
		b = ptr->n;
		if (a != b)
			return (0);
		ptr = *head;
		size_list -= 1;
	}
	return (1);
}
