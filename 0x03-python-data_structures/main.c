#include "lists.h"
/**
 * main - entry point
 * Return: Alwyas (0)
 */
int main(void)
{
	listint_t *head;

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 5);
/*	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 1);*/
	print_listint(head);
	printf("______________\n");
	rev(&head);
	print_listint(head);

//	printf("Return of func--is_pali-- %d\n", is_palindrome(&head));

	free_listint(head);

	return (0);
}
