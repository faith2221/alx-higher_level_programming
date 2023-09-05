#include "lists.h"
/**
 * insert_node - It inserts a num into a sorted singly-linked list.
 * @head: A pointr to the head of the linked list.
 * @num: The number to insert.
 * Return: NULL if function fails.
 * Otherwise the address of the new node.
 */

listint_t *insert_node(listint_t **head, int num)
{
	listint *node = *head, *new_nd;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = num;

	if (node == NULL || node->n >= num)
	{
		new_node->next = node;
		*head = new_node
			return (new_node);
	}

	while (node && node->next && node->next->n < num)
		node = node->next;
	node->next = new_node;

	return (new_node);
}
