#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks cycle of linked lists
 * @list: pointer to head of list
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
    listint_t *slow, *fast;
    slow = fast = list;
   
    while(slow && fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
           return (1);
        }
    }
    return (0);
}