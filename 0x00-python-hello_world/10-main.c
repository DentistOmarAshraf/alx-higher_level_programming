#include "lists.h"

/**
 * main - Entry point
 *
 * Return: alwyas (0)
 */

int main(void)
{
	listint_t *head;
	listint_t *cur;
	listint_t *temp;
	int i;

	head = NULL;
	add_nodeint(&head, 0);
	add_nodeint(&head, 1);
	add_nodeint(&head, 2);
	add_nodeint(&head, 3);
	add_nodeint(&head, 4);
	add_nodeint(&head, 98);
	add_nodeint(&head, 402);
	add_nodeint(&head, 1024);
	print_listint(head);
	
	if (!check_cycle(head))
		printf("there is no cycle!\n");
	else
		printf("positive Cycle\n");

	cur = head;
	for (i = 0 ; i < 4 ; i++)
		cur = cur->next;
	temp = cur->next;
	cur->next = head;

	if (!check_cycle(head))
		printf("there is no cycle!\n");
	else
		printf("positive Cycle\n");

	cur->next = temp;
	free_listint(head);

	return (0);
}
