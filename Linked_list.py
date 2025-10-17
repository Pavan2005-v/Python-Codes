
struct node
{
	int data;
	struct node *next;
};
typedef struct node NODE;
NODE *create();
void insertAtBegin(int);
void insertAtEnd(int);
void insertAtAnywhere(int);
void deleteAtBegin();
void deleteAtEnd();
void deleteAtAnywhere();
void traverse();
void reverse(NODE*);
int size();
NODE *head=NULL;
NODE *create()
{
	NODE temp=(NODE)malloc(sizeof(NODE));
	return temp;
}
void insertAtBegin(int n)
{
	NODE *temp=create();
	temp->data=n;
	if(head==NULL){
		head=temp;
		head->next=NULL;
	}
	else
	{
		temp->next=head;
		head=temp;
	}
}
void insertAtEnd(int n)
{
	NODE *t,*temp=create();
	temp->data=n;
	temp->next=NULL;
	if(head==NULL)
	{
		head=temp;
	}
	else
	{
		t=head;
		while(t->next!=NULL)
		t=t->next;
		t->next=temp;
	}
}
void insertAtAnywhere(int n)
{
	NODE *t,*prev,*temp;
	int p,loc=0;
	printf("Enter position to insert:");
	scanf("%d",&p);
	if(head==NULL)
	{
		printf("No such postion:\n");
	}
	else if(p==size()+1)
	insertAtEnd(n);
	else if(p>size())
	printf("No Such position\n");
	else
	{
		temp=create();
		temp->data=n;
		t=prev=head;
		while(t->next!=NULL)
		{
			loc++;
			if(loc==p)
			break;
			prev=t;
			t=t->next;
		}
		prev->next=temp;
		temp->next=t;
		
	}
}
int size()
{
	NODE *temp=head;
	int l=0;
	while(temp!=NULL)
	{
		l++;
		temp=temp->next;
	}
	return l;
}
void deleteAtBegin()
{
	NODE *temp;
	if(head==NULL)
	{
		printf("List is empty!!!\n");
		return;
	}
	else
	{
		printf("%d is removed\n",head->data);
		temp=head;
		head=head->next;
		free(temp);
	}
}
void deleteAtEnd()
{
	NODE *temp,*prev;
	if(head==NULL)
	{
		printf("List is empty!!!\n");
		return;
	}
	else
	{
		temp=head;
		while(temp->next!=NULL)
		{
			prev=temp;
			temp=temp->next;
		}
		printf("%d is removed\n",temp->data);
		prev->next=NULL;
		free(temp);
	}
}
void deleteAtAnywhere()
{
	NODE *temp,*prev;
	int p,loc=0;
	printf("Enter the location:");
	scanf("%d",&p);
	if(head==NULL)
	{
		printf("List is Empty!!!\n");
	}
	else if(p==size())
	deleteAtEnd();
	else if(p==1)
	deleteAtBegin();
	else if(p>size())
	printf("No such position\n");
	else
	{
		temp=head;
		while(temp->next!=NULL)
		{
			loc++;
			if(loc==p)
			break;
			prev=temp;
			temp=temp->next;
		}
		printf("%d is removed\n",temp->data);
		prev->next=temp->next;
		free(temp);
	}
}
void reverse(NODE *t)
{
	if(t==NULL)
	return;
	else
	{
		reverse(t->next);
		printf("->%d",t->data);
	}
}
void traverse()
{
	NODE *temp;
	if(head==NULL)
	printf("List is empty!!!\n");
	else
	{
		temp=head;
		while(temp!=NULL)
		{
			printf("->%d",temp->data);
			temp=temp->next;
		}
		printf("\n");
	}	
}
int main()
{
	int ch,n;
	
	do
	{
		printf("1.insert at begin\n2.Insert at end\n");
		printf("3.insert at anywhere\n4.Delete at begin\n");
		printf("5.delete at ending\n6.delete at anywhere\n");
		printf("7.traverse\n8.reverse\nEnter your choice:");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:printf("Enter an Element to insert:");
				   scanf("%d",&n);
				   insertAtBegin(n);
				   break;
			case 2:printf("Enter an Element to insert:");
				   scanf("%d",&n);
				   insertAtEnd(n);
				   break;
			case 3:printf("Enter an Element to insert:");
				   scanf("%d",&n);
				   insertAtAnywhere(n);
				   break;
			case 4:deleteAtBegin();
				   break;
			case 5:deleteAtEnd();
				   break;
			case 6:deleteAtAnywhere();
				   break;
			case 7:traverse();
				   break;
			case 8:if(head==NULL) 
				   printf("List is Empty!!!");
				   else
				   reverse(head);
				   printf("\n");
				   break;
			default:exit(0);
		}
	}while(1);
	return 0;
}