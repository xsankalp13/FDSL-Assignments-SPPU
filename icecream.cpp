#include<iostream>
using namespace std;

struct node
{
    int roll;
    node* next;
};

node* head=NULL;//total number of students;
node* headA=NULL;//total number of students who likes vanilla
node* headB=NULL;//total number of students who like butterscotch;




void eitheroneButnorBoth(){
    node* ptr1;
    node* ptr2;
    node* ptr;
    node*temp = new node;
    while(ptr1->next != NULL && ptr2->next!=NULL){
        if(ptr1->roll == ptr2->roll){
            ptr1 = ptr1->next;
            ptr2 = ptr2->next; 
        }else{
            temp->roll = ptr1->roll;
            temp->next = ptr;
            ptr = temp;
            ptr2=ptr2->next;
        }
        
    }
    while(ptr1->next!=NULL){
        temp->roll = ptr1->roll;
        temp->next = ptr;
        ptr = temp;
        ptr1=ptr1->next;
    }
    while(ptr2->next!=NULL){
        temp->roll = ptr2->roll;
        temp->next = ptr;
        ptr = temp;
        ptr2=ptr2->next;
    }


    while(ptr->next != NULL){
        cout<<"Students who likes either one but nor both: ";
        cout<<ptr->roll<<" ";
    }
    cout<<endl;
}


node both(){
    // node* ptr1;
    // node* ptr2;
    // node* ptr = NULL;
    // node* temp = new node;
    // ptr1 = headA;
    // ptr2 = headB;
    // while(ptr1->next!=NULL){
    //     while(ptr2->next!=NULL){
    //         if(ptr1->roll == ptr2->roll){
    //             temp->roll = ptr1->roll;
    //             temp->next = ptr;
    //             ptr = temp;
    //         }
    //     }
    // }

    node* newPointerForVanilla;
    node* newPointerforButter;
    newPointerForVanilla = headA;
    newPointerforButter = headB;
    node* Both = NULL;
    node* temp = new node;
    while(newPointerForVanilla->next!=NULL){
        while(newPointerforButter->next!=NULL){
            if(newPointerforButter->roll == newPointerForVanilla->roll){
                temp->roll = newPointerforButter->roll;
                temp->next = Both;
                Both = temp;
            }
        }
    }

    while(Both->next!=NULL){
        cout<<"Roll numbers of students who likes vanilla and butter both: ";
        cout<<Both->roll<<" ";
    }
    return *Both;

}

void nor(){
    node* newPointerForVanilla;
    node* newPointerforButter;
    newPointerForVanilla = headA;
    newPointerforButter = headB;
    node* Both = NULL;
    node* temp = new node;
    while(newPointerForVanilla->next!=NULL){
        while(newPointerforButter->next!=NULL){
            if(newPointerforButter->roll == newPointerForVanilla->roll){
                temp->roll = newPointerforButter->roll;
                temp->next = Both;
                Both = temp;
            }
        }
    }
    node* ptr1 = &both();
    node* ptr2;
    node* ptr;
    node* temp = new node;
    ptr2 = head;
    while(ptr2->next!=NULL){
        while(ptr1->next != NULL){
            if(ptr2->roll == ptr1->roll){
                continue;
            }else{
                temp->roll = ptr2->roll;
                temp->next = ptr;
                ptr = temp;
            }
        }
    }

}

int main(){

    int n;
    cout<<"Enter the number of students: ";
    cin>>n;
    for(int i = 0; i<n;i++){
        int roll;
        cout<<"Enter the roll number for"<<i+1<<"th student: ";
        cin>>roll;
        node* temp = new node;
        temp->roll = roll;
        temp->next=head;
        head = temp;
    }
    int k;
    cout<<"Enter the students Who likes Vanilla: ";
    cin>>k;
    for(int i =0 ; i<k;i++){
        int roll;
        cout<<"Enter the roll number for"<<i+1<<"th student: ";
        cin>>roll;
        node* temp = new node;
        temp->roll = roll;
        temp->next = headA;
        headA = temp;
    }
    cout<<"Enter the number of students Who likes butterscotch: ";
    cin>>k;
    for(int i=0;i<k;i++){
        int roll;
        cout<<"Enter the roll number for"<<i+1<<"th student: ";
        cin>>roll;
        node* temp = new node;
        temp->roll = roll;
        temp->next = headB;
        headA = temp;
    }
    bool flag = true;
    while(flag){
        cout<<"***MENU***\n1.Both\n2.either one but nor both\n3.nor any \nEnter your choice: ";
        int ch;
        cin>>ch;
        if(ch == 1){
            both();
        }
        else if(ch == 2){
            eitheroneButnorBoth();
        }else if(ch == 3){
            nor();
        }
        cout<<"Do you want to continue(y/n): ";
        char a;
        cin>>a;
        if(a=='y'||a=='Y'){
            continue;
        }else{
            flag = false;
        }
    }

    return 0;
}