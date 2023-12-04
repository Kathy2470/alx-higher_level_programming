#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

listint_t *reverse_list(listint_t *head);

int is_palindrome(listint_t **head);

int main(void)
{
    listint_t *head = NULL;
    int result;


    result = is_palindrome(&head);

    if (result)
        printf("The linked list is a palindrome.\n");
    else
        printf("The linked list is not a palindrome.\n");

    return 0;
}

listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *current = head, *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = *head;
    listint_t *second_half, *temp;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL)
        slow = slow->next;

    second_half = reverse_list(slow);
    temp = second_half;

    while (temp != NULL)
    {
        if ((*head)->n != temp->n)
            return 0;

        *head = (*head)->next;
        temp = temp->next;
    }

    prev_slow->next = reverse_list(second_half);

    return 1;
}
