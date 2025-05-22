#ifndef Vol
#define Vol

#include <iostream>
#include <vector>
#include <cmath>
#include "vector.hpp"
#include "matrix.hpp"


struct Tempreture {

    double integral_x(double(*f)(double x, double y), double a, double b, double y_c);

    double integral_y(double(*f)(double x, double y), double a, double b, double x_c);

    double fu(Matrix T, double i, double j, double(*dt_dn)(double x, double y),double si);

    std::vector<Matrix> temp(Matrix mm, double g, double(*dt_dn)(double x, double y), double t_p);

    std::vector<Matrix> tempmat(Matrix mm, double g, double(*dt_dn)(double x, double y), double t_p);

};

#endif