#include <iostream>
#include <deque>
#include <string>
#include <vector>

template<typename Container = std::deque<int>>
class Stack {
    
    Container container;

    public:

    Container::value_type top() {
        if (not(is_empty()))
        return *(container.cend() - 1);

        else
            throw std::runtime_error("Stack is empty");
    }

    void pop() {
        if (not(is_empty()))
            container.pop_back();
        else
            throw std::runtime_error("Stack is empty");
    }

    void push (Container::value_type value) {
        container.push_back(value);
    }

    int size() const {
        int r = 0;
        for (auto it = container.cbegin(); it != container.cend(); ++it)
            ++r;
        return r;}

    bool is_empty() {
        return container.cbegin() == container.cend();
    }
};

template<>
class Stack<std::string> {

std::string container;

public:

char top() {
    if (not(is_empty())){
        std::cout<<"it is string top ";
        return *(container.cend() - 1);}

    else
        {throw std::runtime_error("Stack is empty");}
    }

    void pop() {
        if (not(is_empty()))
            container.pop_back();
    }

    void push (char value) {
        container.push_back(value);
    }

    int size() const {
        int r = 0;
        for (auto it = container.cbegin(); it != container.cend(); ++it)
            ++r;
            return r;}

    bool is_empty() {
        return container.cbegin() == container.cend();
    }
};

int main (){
    Stack<> d;
    d.push(2);
    d.pop();
    d.push(5);
    std::cout<<d.is_empty()<<std::endl;
    std::cout<<d.size()<<std::endl;
    std::cout<<d.top()<<std::endl;
    
    Stack<std::string> ch;
    ch.push('a');
    ch.push('b');
    std::cout << "Top: " << ch.top() << std::endl;
    ch.pop();
    std::cout << "size:  " << ch.size() << std::endl;

    return 0;
}



