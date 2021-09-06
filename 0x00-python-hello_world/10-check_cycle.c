#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: head of the linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = NULL, *slow = NULL;

	if (!list)
		return (0);
	fast = list->next;
	slow = list;

	while (fast && fast->next)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
