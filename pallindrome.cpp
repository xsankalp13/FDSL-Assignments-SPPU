#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main(){
    string s;
    cout<<"Enter the string: ";
    stack<char> stack;
    cin.ignore(0);
    getline(cin,s);
    cout<<s<<endl;
    int n=s.length();
    string newstr="";
    for(int i = 0; i<n;i++){
        if(s[i]==' '){
            continue;
        }else{
            newstr = newstr+s[i];
        }
    }
    n = newstr.length();
    for(int i = 0; i<n; i++){
        stack.push(newstr[i]);
    }
    bool flag = true;
    cout<<newstr<<endl;
    for(int i = 0; i<n;i++){
        if(stack.top() == newstr[i]){

            stack.pop();

        }else{
            cout<<stack.top()<<" ";
            flag = false;
            break;
        }
    }
    if(flag){
        cout<<"Pallindrome"<<endl;
    }else{
        cout<<"Not";
    }
}

