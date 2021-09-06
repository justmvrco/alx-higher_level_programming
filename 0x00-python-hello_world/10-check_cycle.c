#include "lists.h"

/**
  * check_cycle - checks if a singly linked list has a cycle.
  * @list: pointer to first element.
  *
  * Return: 1 if cycle is found 0 if not.
  */
int check_cycle(listint_t *list)
{
	listint_t *current, *next_node;

	if (list == NULL)
		return (0);

	current = list;
	next_node = list;

	while (current && next_node && next_node->next)
	{
		current = current->next;
		next_node = next_node->next->next;
		if (current == next_node)
			return (1);
	}
	if (current != next_node)
		return (0);
	return (1);
}
