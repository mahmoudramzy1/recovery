#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * chech_cycle - checks if the linkes list is cyclic
 * @list: pointer to the head of the list
 * Return: 1 if there is cycle in the list
 */
int check_cycle(listint_t *list)
{
	listint_t *step = list;
	listint_t *twosteps = list;

	while (twosteps != NULL && twosteps->next != NULL)
	{
		step = step->next;
		twosteps = twosteps->next->next;
		if (step == twosteps)
			return (1);
	}
	return (0);

}
