#include "lists.h"

/**
 * reverse_listint - Reverses a singly_linked listint_t list.
 * @head: A pointer  to the starting of the list to reverse.
 * Return: A pointer to the head of the reversed list.
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Check if a linked list is a palindrome.
 * @head: Pointer to the head of the list.
 * Return: 1 if it's a palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *rev = *head;
	listint_t *mid = *head;
	listint_t *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		rev = rev->next->next;
		if (!rev)
		{
			dup = mid->next;
			break;
		}
		if (!rev->next)
		{
			dup = mid->next->next;
			break;
		}
		mid = mid->next;
	}
	reverse_listint(&dup);
	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!dup)
		return (1);
	return (0);
}

