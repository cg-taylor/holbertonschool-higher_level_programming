#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle
 * @list: the list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	do {
	       	slow = slow->next;
	       	fast = fast->next->next;

		if (slow == fast)
			return (1);
	} while (slow && fast && fast->next);
	return (0);
}
