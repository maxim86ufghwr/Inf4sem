#include <iostream>
#include <cstdlib>
#include "vector.hpp"
#include "matrix.hpp"
#include "vector.cpp"
#include "matrix.cpp"

int main() {
	Matrix<double> m1{3, 3, 1};
    m1(1,2) = 3;
    m1.transpose();
    m1.print_m();
    std::cout<<m1.get_rows()<<"<-get_rows"<<std::endl;
    Matrix<double> m2 = m1;
    m2(1,2) = 2;
    m2(1,1) = 2;
    m2.print_m();
    double t = m2.get_det();
    std::cout<<t<<"<-get_det"<<std::endl;
    Matrix<double> E = Matrix<double>::Identity(3, 3);
    E.print_m();
    Matrix<double> m3 = Matrix<double>::getSpecificDeterminant(3, 1);
    m3.print_m();
    double de = m3.get_det();
    std::cout<< de <<"<-get_det"<<std::endl;
    return 0;
}