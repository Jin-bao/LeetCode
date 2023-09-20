#include <stdio.h>
#include <stdlib.h>

struct ListNode {
  int val;
  struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* L1, struct ListNode* L2) {
  struct ListNode *head=NULL, *tail=NULL;
  int a=0, b=0, sum=0, carry=0, rem=0;

  while (L1!=NULL || L2!=NULL) {
    a = L1 ? L1->val : 0;
    b = L2 ? L2->val : 0;
    sum = a+b + carry;
    rem = sum%10;
    carry = sum/10;

    if (head==NULL) {
      head = tail = malloc(sizeof(struct ListNode));
      tail->val = rem;
      tail->next = NULL;
    }
    else {
      tail->next = malloc(sizeof(struct ListNode));
      tail = tail->next;
      tail->val = rem;
      tail->next = NULL;
    }

    if (L1!=NULL) {
      L1 = L1->next;
    }
    if (L2!=NULL) {
      L2 = L2->next;
    }
  }
  
  if (carry>0) {
    tail->next = malloc(sizeof(struct ListNode));
    tail = tail->next;
    tail->val = carry;
    tail->next = NULL;
  }

  return head;
}

void foreach(struct ListNode* L) {
  while (L!=NULL) {
    printf("%d", L->val);
    L = L->next;
  }
}

int main (void) {
  struct ListNode node1 = { 2, NULL };
  struct ListNode node2 = { 4, NULL };
  struct ListNode node3 = { 7, NULL };
  struct ListNode pnode1 = { 5, NULL };
  struct ListNode pnode2 = { 6, NULL };
  struct ListNode pnode3 = { 4, NULL };

  node1.next = &node2;
  node2.next = &node3;
  pnode1.next = &pnode2;
  pnode2.next = &pnode3;

  foreach(&node1);
  printf("\n");
  foreach(&pnode1);
  printf("\n");

  struct ListNode *LN = addTwoNumbers(&node1, &pnode1);
  foreach(LN);
  printf("\n");

  return 0;
}
