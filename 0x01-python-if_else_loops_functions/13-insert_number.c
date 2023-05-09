#include "lists.h"

/**
 * insert_node - Inserts number in sorted LL
 * @head: Where to insert
 * @number: What to insert
 *
 * Return: Address or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *before = NULL, *new = NULL, *temp = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head != NULL)
	{
		before = *head;
		if (number <= before->n)
		{
			new->next = before;
			*head = new;
		}
		else
		{
			while (before->next)
			{
				if (number <= before->next->n)
				{
					temp = before->next;
					before->next = new;
					new->next = temp;
					return (*head);
				}

				before = before->next;
			}
			temp = before->next;
			before->next = new;
			new->next = temp;
		}
		return (*head);
	}
	new->next = NULL;
	*head = new;
	return (*head);
}

