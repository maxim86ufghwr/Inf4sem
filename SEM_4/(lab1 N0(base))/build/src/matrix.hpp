#ifndef MATRIX_HPP
#define MATRIX_HPP

template<typename T>
class Matrix {
	vector<T> data;
	unsigned cols, rows;

public:
	Matrix(unsigned rows, unsigned cols, T value = 0);

	static Matrix Identity(unsigned rows, unsigned cols);

	static Matrix getSpecificDeterminant(unsigned n, T determinant);

    unsigned int get_rows() const;
    unsigned int get_cols() const;


	T& operator()(unsigned row, unsigned col);
	T operator()(unsigned row, unsigned col) const;

    Matrix& transpose();

    Matrix transpose() const;

    void change_row(unsigned int r1, unsigned int r2);

    void change_col(unsigned int c1, unsigned int c2);

    void sr1_r2(unsigned int r1, unsigned int r2);

    void mr1_r2(unsigned int r1, unsigned int r2);

    void mr_a(unsigned int r, T a);

    void print_m();

    T get_det();
};

#endif