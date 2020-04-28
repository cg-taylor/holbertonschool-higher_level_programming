#include "lists.h"

/**
 * insert_node - insert a new node into a sorted singly linked list
 * @head: double pointer to the head of the list
 * @number: the value to insert
 *
 * Return: pointer to the new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *previous, *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (number < (*head)->n)
	{
		new->next = (*head)->next;
		*head = new;
		return (new);
	}

/* Find node with n larger than number */
	while ((number > current->n) && current->next)
	{
		previous = current;
		current = current->next;
	}

	if (current->next == NULL && number >= current->n)
	{
		new->next = NULL;
		current->next = new;
	}
	else
	{
		new->next = current;
		previous->next = new;
	}
	return (new);
}
