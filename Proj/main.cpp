#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include "vector.hpp"
#include "matrix.hpp"
#include "vector.cpp"
#include "matrix.cpp"
#include "volume.hpp"
#include "volume.cpp"


int main() {
    Matrix M{10, 10, 0};
    auto f_1 = [](double x, double y){return (x == 0.5 or x == 0.95) ? double(0) : double(x); };
    double q = 0.4;

    for (double i = 0; i < M.get_cols(); i++){
        for (double j = 0; j < M.get_cols(); j++){
            M(i, j) = (j / double(M.get_cols()) + 0.05) * (j / double(M.get_cols()) + 0.05) / 2;
    }
    }
    Tempreture b{};
    
    auto f_2 = [](double x, double y){return (x == 0.05 or x == 0.995) ? double(0) : double(x); };
    
    std::vector<Matrix> f = b.temp(M, q, f_2, 1);

    Matrix M1{100, 100, 0};
    for (double i = 0; i < M1.get_cols(); i++){
        for (double j = 0; j < M1.get_cols(); j++){
            M1(i, j) = (j / double(M1.get_cols())+0.005) * (j / double(M1.get_cols())+0.005) / 2;
    }
    }

    M.print_m();

    std::vector<Matrix> f1 = b.temp(M1, q, f_1, 0.025);
}