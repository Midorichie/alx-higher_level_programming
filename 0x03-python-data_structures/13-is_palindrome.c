#include <stdio.h>
#include "lists.h"

void reverse(listint_t **head);
int compare_lists(listint_t *head, listint_t *middle, int len);

/**
 * is_palindrome - checks whether a singly linked list is a palindrome
 * @head: pointer tp a pointer of the first node in the list that is passed
 * Return: 0 if a palindrome is not detected, else 1
 */

int is_palindrome(listint_t **head)
{
	int len, m;
	listint_t *tmp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
		return (1);
	tmp = *head;
	middle = *head;

	for (len = 0; tmp != NULL; len++)
		tmp = tmp->next;

	len = len / 2;

	for (m = 1; m < len; m++)
		middle = middle->next;
	if (len % 2 != 0 && len != 1)
	{
		middle = middle->next;
		len = len - 1;
	}
	reverse(&middle);
	m = compare_lists(*head, middle, len);

	return (m);
}

/**
 * compare_lists - compare two lists
 * @head: A pointer to the head node
 * @middle: pointer to the middle node
 * @len: length of the list
 * Return: 1 if the same, else 0
 */

int compare_lists(listint_t *head, listint_t *middle, int len)
{
	int m;

	if (head == NULL || middle == NULL)
		return (1);
	for (m = 0; m < len; m++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);
}

/**
 * reverse - reverses a list
 * @head: pointer to the head to reverse
 */

void reverse(listint_t **head)
{
	listint_t *current;
	listint_t *next;
	listint_t *prev;

	if (head == NULL || *head == NULL)
		return;

	prev = NULL;
	current = *head;
	while (current != NULL)
	{

		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
