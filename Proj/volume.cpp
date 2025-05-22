#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include "vector.hpp"
#include "matrix.hpp"
#include "volume.hpp"


    double Tempreture::integral_x(double(*f)(double x, double y), double a, double b, double y_c) {
    double step = (b - a) / 10;
    double area = 0.0;
    for (int i = 0; i < 10; i ++) {
        area += f(a + (i + 0.5) * step, y_c) * step;
        }
        return area;
    }

    double Tempreture::integral_y(double(*f)(double x, double y), double a, double b, double x_c) {
        double step = (b - a) / 10;
        double area = 0.0;
        for (int i = 0; i < 10; i ++) {
            area += f(x_c, a + (i + 0.5) * step) * step;
    }
        return area;
    }

    double Tempreture::fu(Matrix T, double i, double j, double(*dt_dn)(double x, double y), double si){
        double delt = 0;

        if (i == 0){
            delt += integral_x(dt_dn, j/si, (j+1)/si, (0.5)/si);
        }
        else {delt += T(i-1, j) - T(i, j);}
        
        if (i == si-1){
            delt += integral_x(dt_dn, j/si, (j+1)/si, 1 - (0.5)/si);
        }
        else {delt += T(i+1, j) - T(i, j);}

        if (j == 0){
            delt += integral_y(dt_dn, i/si, (i+1)/si, (0.5)/si);
        }
        else {delt += T(i, j-1) - T(i, j);}
        
        if (i == si-1){
            delt += integral_y(dt_dn, i/si, (i+1)/si, 1 - (0.5)/si);
        }
        else {delt += T(i, j+1) - T(i, j);}
        
        return delt;
    }
    
    std::vector<Matrix> Tempreture::temp(Matrix mm, double g, double(*dt_dn)(double x, double y), double t_p){
	    
        std::vector<Matrix> data_b{};
        data_b.push_back(mm);
        double si = mm.get_rows();
        Matrix T_n = Matrix::Zero(si, si);
        std::vector<Matrix>::iterator T = data_b.end();

        double h = 1/si;
        double dt = h * h * g * 0.4;
        std::ofstream out;
        
        if (si <= 11)
            out.open("data_1.txt");
        else
            if (si <= 101)
                out.open("data_2.txt");
            else
                out.open("data_3.txt");
    
        for (int t = 0; t < t_p/dt; t++){
            T_n = Matrix::Zero(si, si);
            T = data_b.end() - 1;
            for (int j = 0; j < si; j++){
                for (int i = 0; i < si; i++){
                    T_n(i,j) = g * dt / (h*h) * fu(*T, i, j, dt_dn, si) + (*T)(i, j);
                        out <<T_n(i, j)<<" ";
            }}
            data_b.push_back(T_n);
            out << std::endl;
            std::cout<<"ok"<<t<<std::endl;
    }
    out.close();
    return data_b;
    }
