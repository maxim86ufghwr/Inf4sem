#ifndef MATRIX_HPP
#define MATRIX_HPP
#include "vector.hpp"

class Matrix {
	vector data{};
	unsigned cols, rows;

    public:
	Matrix(unsigned rows, unsigned cols, double value = 0);

	static Matrix Identity(unsigned rows, unsigned cols);

	static Matrix getSpecificDeterminant(unsigned n, double determinant);

    unsigned int get_rows() const;
    unsigned int get_cols() const;


	double& operator()(unsigned row, unsigned col);
	double operator()(unsigned row, unsigned col) const;

    Matrix& transpose();

    Matrix transpose() const;

    void change_row(unsigned int r1, unsigned int r2);

    void change_col(unsigned int c1, unsigned int c2);

    void sr1_r2(unsigned int r1, unsigned int r2);

    void mr1_r2(unsigned int r1, unsigned int r2);

    void mr_a(unsigned int r, double a);

    void print_m();

    double get_det();
};

#endif