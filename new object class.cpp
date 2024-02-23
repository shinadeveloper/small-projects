#include<iostream>
#include<map>
#include<vector>
#include<set>
using namespace std;
class Student{
    public:
    Student(int givenroll_no,string giventext,int givenmarks,string givenremark){
        roll_no=givenroll_no;
        name=giventext;
        marks=givenmarks;
        remark=givenremark;
    }
    int getroll_no() const {return roll_no;}
    string getname() const {return name;}
    int getmarks() const {return marks;}
    string getremarks() const {return remark;}
     bool operator<(const Student& other) const {
        return roll_no < other.roll_no;
    }
    int roll_no;
    string name;
    int marks;
    string remark;
};
class management{
    public:
    set<vector<int>> dataset;
    void addstudent(int roll_no,string name,int marks,string remark){
        students.insert(Student(roll_no,name,marks,remark));
    }
    void searchname(int roll_no){
        bool flag=false;
        for(auto student:students){
            if(student.getroll_no()==roll_no){
                cout<<student.getname()<<endl;;
                flag=true;
                return;
            }
        }
        if (flag==false){
            cout<<"no such element"<<endl;}
        return;
        
    }
    void display(){
        for (auto student:students){
            cout<<student.getmarks()<< " "<<student.getroll_no()<<"  "<<student.getname()<<" "<<student.getremarks()<<endl;
        }
    }
    private:
    set<Student> students;
};
int main(){
    management yay;
    yay.addstudent(123,"raju",23,"kutta munda");
    yay.display();
    yay.searchname(123);
    yay.searchname(546);
}