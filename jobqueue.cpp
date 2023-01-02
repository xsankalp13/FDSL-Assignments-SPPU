#include<iostream>
using namespace std;
struct queue{
    int data[10];
    int front,rear;
};

class Queue{
    queue q;
    public:
    Queue(){
        q.front=q.rear=-1;
    }
    int isempty();
    int isFull();
    void enqueue(int);
    int delqueue();
    void display();
};

int Queue::isempty(){
    return(q.front==q.rear)?1:0;
}
int Queue::isFull(){
    return(q.rear == 9)?1:0;
}
void Queue::enqueue(int n){
    //Queue temp;
    if(q.front!=-1){
        for(int i = q.front;i<=q.rear;i++){
            int temp = q.data[q.front];
            q.data[q.front]=q.data[q.rear];
            q.data[q.rear]=temp;
        }
        --q.front;
        q.data[q.rear]=n;
    }
    q.data[++q.rear] = n;
}
int Queue::delqueue(){
    return q.data[++q.front];
}
void Queue::display(){
    for(int i= q.front;i<=q.rear;i++){
        cout<<q.data[i]<<" ";
    }
    cout<<"\n";
}
int main(){
    Queue q;
    bool flag = true;
    while(flag){
    cout<<"****MENU****\n1.ADD JOB QUEUE\n2.DELETE JOB QUEUE\n3.DISPLAY ALL JOB QUEUES\n4.EXIT\nENTER YOUR CHOICE: ";
    int ch;
    cin>>ch;
    switch(ch){
        case 1:
        if(!q.isFull()){
            cout<<"Enter job id: ";
            int id;
            cin>>id;
            q.enqueue(id);
        }else{
            cout<<"\nQUEUE IS FULL!!!"<<endl;
        }
        break;
        case 2:
        if(!q.isempty()){
            cout<<"id number: "<<q.delqueue()<<" is deleted!"<<endl;
        }else{
            cout<<"JOB QUEUE IS EMPTY!!!"<<endl;
        }
        break;
        case 3:
        if(!q.isempty()){
            q.display();
            cout<<endl;
        }else{
            cout<<"QUEUE IS EMPTY"<<endl;
        }
        break;
        case 4:
        cout<<"OK EXIT!"<<endl;
        flag = false;
        break;
        default:
        cout<<"****Wrong input forced Shut Down****"<<endl;
        flag = false;
        break;
    }
    }
}