#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: int
 * @next: pointer to next node
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *);
listint_t *add_nodeint_end(listint_t **, const int n);
void free_listint(listint_t *);
listint_t *insert_node(listint_t **, int);

#endif
