#include <stdio.h>
#include "lists.h"

listint_t *reverse(listint_t **head);

/**
 * is_palindrome - Check if singly linked list is a palindrome
 * @head: Pointer to the head of the list
 * Return: 1 if its a palindrome, 0 if it's not
 */
int is_palindrome(listint_t **head)
{
	size_t len, i;
	listint_t *rev, *temp, *x;

	len = 0;

	if ((*head)->next == NULL || *head == NULL)
		return (1);

	temp = *head;

	while (temp)
	{
		++len;
		temp = temp->next;
	}

	temp = *head;

	for (i = 0; i < ((len / 2) - 1); i++)
		temp = temp->next;

	if ((len % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rev = reverse(&temp);
	x = rev;

	temp = *head;

	while (rev)
	{
		if (temp->n != rev->n)
			return (0);

		temp = temp->next;
		rev = rev->next;
	}

	reverse(&x);

	return (1);
}

/**
 * reverse - Reverses a singly-linked list
 * @head: Pointer to the head node
 * Return: Pointer to the new head node after reversal
 */
listint_t *reverse(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

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
