#include<iostream>
using namespace std;

class Rectangle{
    protected:
       int width;
       int height;

    public:
      void red_input()
      {
        cin>> width>> height;
      }       
      void display(){
        cout<<width<<" "<<height<<endl;
      }
};

class RectangleArea:public Rectangle
{
   void display()
   {
    cout<<width*height<<endl;
   }
};
int main(){
    
    
    return 0;
}