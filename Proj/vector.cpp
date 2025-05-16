#include <iostream>
#include <cstdlib>
#include "vector.hpp"


vector::vector(): top(0), capacity(0), mas(NULL){}


vector::~vector(){
    delete[] mas;
    mas = NULL;
}


vector::vector(const vector &rhs): top(rhs.top), capacity(rhs.capacity){
    mas = new double[capacity];
    for (int i = 0; i < top ; i++)
        mas[i] = rhs.mas[i];
}


vector& vector::operator=(const vector & rhs){
	if (this == &rhs) return *this;
	top = rhs.top;
    capacity = rhs.capacity;
	delete mas;
	mas = new double[capacity];
	for (int i = 0; i < top ; i++)
        mas[i] = rhs.mas[i];
	return *this;
	}


vector::vector(vector && rhs){
    top = rhs.top;
    capacity = rhs.capacity;
    mas = rhs.mas;
    rhs.top = 0;
    rhs.capacity = 0;
    rhs.mas = nullptr;
}


vector& vector:: operator=(vector && rhs){
    top = rhs.top;
    capacity = rhs.capacity;
    delete[] mas;
    mas = rhs.mas;
    rhs.top = 0;
    rhs.capacity = 0;
    rhs.mas = nullptr;
    return *this;
}


double& vector::operator()(unsigned row) {
    return mas[row];
}


double vector::operator()(unsigned row) const{
    return mas[row];
}
 

bool vector::push_back(const double& d){
    if (capacity == top) {
    capacity = (capacity + 1) * 2;
    double* tm = new double[capacity];

    if (tm == NULL or (mas == NULL and top != 0) ){return 0;}

    for (int i = 0; i < (capacity - 1) / 2; i++)
        tm[i] = mas[i];
    
    delete [] mas;
    mas = tm;
    }
    mas[top++] = d;
    return 1;
}


double vector::pop_back(){
    if (top == 0) return double();
    return mas[--top];
}


bool vector::resize( unsigned int new_capacity){
    double* tm = new double[new_capacity];
    if (tm == NULL or (mas == NULL and top != 0)){return 0;}
    if (new_capacity > top){
        for (int i = 0; i < top; i++)
            tm[i] = mas[i];
        capacity = new_capacity;
    }
    else {
        for (int i = 0; i < new_capacity; i++)
            tm[i] = mas[i];
        capacity = new_capacity;
        top = new_capacity;
    }
    delete [] mas;
    mas = tm;
    return 1;
}


void vector::shrink_to_fit(){
    double* tm = new double[top];
    for (int i = 0; i < top; i++)
        tm[i] = mas[i];

    delete [] mas;
    mas = tm;
    capacity = top;
    }


void vector::clear(){
    top = 0;
    }


void vector::print_vector(){
    std::cout << "capacity: " << capacity << " top: " << top << std::endl;
    for (unsigned int i = 0; i < top; i++)
    std::cout << mas[i] << std::endl;
    std::cout << "print_vector" << std::endl;
}
