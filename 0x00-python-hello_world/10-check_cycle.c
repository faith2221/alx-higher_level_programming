#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle.
 * @list: The linked list to check.
 * Return: 1 if the list has a cycle.
 * 0 otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *chameleon = list;
	listint_t *lizard = list;

	if (!list)
		return (0);
	while (chameleon && lizard && lizard->next)
	{
		chameleon = chameleon->next;
		lizard = lizard->next->next;
		if (chameleon == lizard)
			return (1);
	}
	return (0);
}
