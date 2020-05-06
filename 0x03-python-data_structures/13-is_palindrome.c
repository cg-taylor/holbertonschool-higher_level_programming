#include "lists.h"

/**
 * reverse_list -
 * @head
 *
 * Return: pointer to new head
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *next;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;

	return (*head);
}

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: double pointer the first element of the linked list to check
 *
 * Return: 0 if it is not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	/* Declarations */
	listint_t *halfway, *endptr;

	if (!(head && *head) || !(*head)->next)
		return (1);

	halfway = *head;
	endptr = *head;

	while (endptr && endptr->next)
	{
		halfway = halfway->next;
		if (endptr->next)
			endptr = endptr->next->next;
	}

	halfway = reverse_list(&halfway);
	endptr = halfway;

	while (halfway && *head != endptr)
	{
		if ((*head)->n != halfway->n)
			return (0);

		*head = (*head)->next;
		halfway = halfway->next;
	}

	return (1);
}
