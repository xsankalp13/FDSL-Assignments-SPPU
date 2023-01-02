// Department of Computer Engineering has student's club named 'Pinnacle Club'. Students of
// second, third and final year of department can be granted membership on request. Similarly
// one may cancel the membership of club. First node is reserved for president of club and last
// node is reserved for secretary of club. Write C++ program to maintain club member‘s
// information using singly linked list. Store student PRN and Name. Write functions to:
// a) Add and delete the members as well as president or even secretary.
// b) Compute total number of members of club
// c) Display members
// d) Two linked lists exists for two divisions. Concatenate two lists.

#include<iostream>
using namespace std;
struct node{
    string name;
    long prn;
    node* next;
};

node* head = NULL;
node* tail = NULL;
void addPersident(){
    string name;
    long prn;
    cout<<"Enter the name of the president: ";
    cin>>name;
    cout<<"Enter the prn number: ";
    cin>>prn;

    node* temp = new node;
    temp->name = name;
    temp->prn = prn;
    temp->next = head;
    head = temp;
}
void addSecretory(){
    string name;
    long prn;
    cout<<"Enter The name of Secretory: ";
    cin>>name;
    cout<<"Enter the prn number: ";
    cin>>prn;
    tail = head;
    while(tail->next!=NULL){
        tail = tail->next;
    }
    node*temp = new node;
    temp->name = name;
    temp->prn = prn;
    tail->next = temp;
    tail = temp;
    temp->next = NULL;    
}

void addmember(){
    string name;
    long prn;
    cout<<"Enter the name of the member: ";
    cin>>name;
    cout<<"Enter the prn number: ";
    cin>>prn;

    node* temp = new node;
    temp->name = name;
    temp->prn = prn;
    temp->next = head->next;
    head->next = temp;
}

void deleteMember(){
    long prn;
    cout<<"Enter the prn number: ";
    cin>>prn;

    if(head->prn == prn){
        head = head->next;
    }else if(tail->prn == prn){
        node*temp;
        temp = head;
        while(temp->next->next != NULL){
            temp=temp->next;
        }
        tail = temp->next;
    }
    else{
        node*temp;
        temp=head;
        while(temp->next->prn != prn&& temp->next != NULL){
            temp=temp->next;
        }
        if(temp->next->prn==prn){
            temp->next = temp->next->next;
        }

    }
}

int totalNumberOfMembers(){
    node*temp;
    temp = head;
    int count=0;
    while(temp->next!=NULL || temp != NULL){
        temp=temp->next;
        count++;
    }
    return count;
}






int main(){




    return 0;
}


