#ifndef TEST_VECTOR_HPP
#define TEST_VECTOR_HPP

class vector {
    double *mas;
    unsigned int top;
    unsigned int capacity;
     
public:
vector();

~vector();

vector(const vector &rhs);

vector& operator=(const vector & rhs);
	
vector(vector && rhs);

vector& operator=(vector && rhs);

double& operator()(unsigned row);
double operator()(unsigned row) const;
    
bool push_back(const double& d);

double pop_back();

bool resize( unsigned int new_capacity);

void shrink_to_fit();

void clear();
    
void print_vector();

};

#endif