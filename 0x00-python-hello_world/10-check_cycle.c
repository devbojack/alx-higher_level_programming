#include "lists.h"

/**
 * check_cycle - Singly linked list cycle checker
 * @list: Singly linked list to check
 *
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	int exists = 0;
	listint_t *header = list, *tailer = list;

	while ((header && tailer) && tailer->next)
	{
		header = header->next;

		if (tailer->next || tailer->next->next)
		{
			tailer = tailer->next->next;
		}
		else
			break;

		if (header == tailer)
		{
			exists = 1;
			break;
		}
	}
	return (exists);
}
