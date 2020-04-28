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
	new->next = NULL;

	if (number < current->n || !current)
	{
		new->next = current;
		*head = new;
		return (*head);
	}

	while (current)
	{
		if (!current->next || new->n < current->next->n)
		{
			new->next = current->next;
			current->next = new;
			return (current);
		}
		current = current->next;
	}
	return (NULL);
}
