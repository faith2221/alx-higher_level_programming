#include "lists.h"
/**
 * insert_node - It inserts a num into a sorted singly-linked list.
 * @head: A pointr to the head of the linked list.
 * @number: The number to insert.
 * Return: NULL if function fails.
 * Otherwise the address of the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (node == NULL || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
			return (new_node);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	node->next = new_node;

	return (new_node);
}
