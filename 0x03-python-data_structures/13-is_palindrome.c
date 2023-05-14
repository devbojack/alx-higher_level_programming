#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

listint_t *reverse_me(listint_t **head);

/**
 * is_palindrome - Checks if is palindrome
 * @head: SLlist head
 *
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *h_start, *h_end, *h_mid;
	size_t i = 0, len = 0;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	h_start = *head;

	while (h_start != NULL)
	{
		len++;
		h_start = h_start->next;
	}

	h_start = *head;

	for (; i < (len / 2) - 1; i++)
	{
		h_start = h_start->next;
	}

	if ((len % 2) == 0 && h_start->n != h_start->next->n)
	{
		return (0);
	}

	h_start = h_start->next->next;
	h_end = reverse_me(&h_start);
	h_mid = h_end;
	h_start = *head;

	while (h_end != NULL)
	{
		if (h_start->n != h_end->n)
		{
			return (0);
		}
		h_start = h_start->next;
		h_end = h_end->next;
	}
	reverse_me(&h_mid);

	return (1);
}

/**
 * reverse_me - Reverses an SLL
 * @head: SLL head
 *
 * Return: reversed SLL pointer
 */
listint_t *reverse_me(listint_t **head)
{
	listint_t *head_node = *head, *next, *prev = NULL;

	while (head_node)
	{
		next = head_node->next;
		head_node->next = prev;
		prev = head_node;
		head_node = next;
	}

	*head = prev;
	return (*head);
}
