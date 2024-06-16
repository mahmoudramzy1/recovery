#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * find_middle - returns the middle node of the list
 * @head: pointer to the head of the list
 * Return: the middle node
 */
listint_t *find_middle(listint_t *head)
{
	listint_t *fast = head, *slow = head;
	
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	return (slow);

}
/**
 * reverse_list - reverse second half of the list
 * @middle: the middle node
 * Return: head of reversed list
 */
listint_t *reverse_list(listint_t *middle)
{
	listint_t *current, *prev, *next_n;

	if (middle == NULL)
		return (NULL);
	prev = NULL;
	current = middle;
	while (current)
	{
		next_n = current->next;
		current->next = prev;
		prev = current;
		current = next_n;
	}
	return (prev);
}
/**
 * is_palindrome - checks if the linked list is palindrome
 * @head: pointer to pointer to the head of list
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *middle;
	listint_t *second_l;

	if (*head == NULL)
		return (1);
	middle = find_middle(*head);
	second_l = reverse_list(middle);
	while(second_l && *head)
	{
		if (second_l->n == (*head)->n)
		{
			second_l = second_l->next;
			*head = (*head)->next;
		}
		else
			return(0);
	}
	return(1);


}
