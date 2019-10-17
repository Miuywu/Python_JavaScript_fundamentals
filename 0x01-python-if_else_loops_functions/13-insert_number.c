#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - insert a node into a sorted linked list
 * @head: start of linked list
 * @number: given value
 * Return: insert node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *copy = *head;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!*head)
	{
		*head = new;
		return (new);
	}
	else if (copy->n > number)
	{
		new->next = copy;
		*head = new;
		return (new);
	}
	while (copy->next && copy->next->n < new->n)
		copy = copy->next;
	new->next = copy->next;
	copy->next = new;
	return (new);
}
