#include <iostream>
#include <cstdlib>
#include "matrix.hpp"
#include "vector.hpp"

template<typename T>
Matrix<T>::Matrix(unsigned rows, unsigned cols, T value) : rows(rows), cols(cols) {
    data.resize(rows * cols);
    for (int i = 0; i < rows * cols; i++){
    data.push_back(value);}
}

template<typename T>
Matrix<T> Matrix<T>::Identity(unsigned rows, unsigned cols){
    Matrix<T> E{rows, cols};
    for (int j = 0; j < rows; j++)
        E(j, j) = 1;
    return E;
    }


template<typename T>
Matrix<T> Matrix<T>::getSpecificDeterminant(unsigned n, T determinant){
        Matrix<T> m = Matrix<T>::Identity(n, n);
        int randNum = rand() % n;
        m(randNum, randNum) = determinant;
        int ran = rand() % (n * 2) + 10;
        for (int i=0; i<ran; i++){
            int ro1 = rand() % n;
            int ro2 = rand() % n;
            if (ro1 != ro2){
            m.sr1_r2(ro1, ro2);}
        }
        return m;
    }
    
	// ... может быть какие-то ещё инициализации для удобства ... //
    template<typename T>
    unsigned int Matrix<T>::get_rows() const { return rows; }
    template<typename T>
    unsigned int Matrix<T>::get_cols() const { return cols; }

	// ... любые "getters", которые вам удобны ... //

    template<typename T>
	T& Matrix<T>::operator()(unsigned row, unsigned col) {
        return data(row * rows + col);
    }
    template<typename T>
	T Matrix<T>::operator()(unsigned row, unsigned col) const{
        return data(row * rows + col);
    }

    template<typename T>
    Matrix<T>& Matrix<T>::transpose(){
        for (unsigned int i = 0; i < rows; i++) {
            for (unsigned int j = 0; j < i; j++) {
                T c = data(j * cols + i);
                std::cout<<data(j * cols + i) << "/" << data(i * rows + j) <<"<-get"<<std::endl;
                data(j * cols + i) = data(i * rows + j);
                data(i * rows + j) = c;
            }
        }
    return *this;
    }

    template<typename T>
    Matrix<T> Matrix<T>::transpose() const {
        Matrix<T> transposed{cols, rows};
        for (unsigned int i = 0; i < rows; i++) {
            for (unsigned int j = 0; j < cols; j++) {
                transposed(i*rows, j) = this(j*cols + i);
            }
        }
        return transposed;
    }

    template<typename T>
    void Matrix<T>::change_row(unsigned int r1, unsigned int r2){
        for (unsigned int j = 0; j < cols; j++) {
            T c = data(r1*cols + j);
            data(r1*cols + j) = data(r2*cols + j);
            data(r2*cols + j) = c;
    }
    }

    template<typename T>
    void Matrix<T>::change_col(unsigned int c1, unsigned int c2){
        for (unsigned int i = 0; i < rows; i++) {
            T c = data(i*cols + c1);
            data(i*cols + c1) = data(c2*cols + c2);
            data(i*cols + c2) = c;
    }
    }

    template<typename T>
    void Matrix<T>::sr1_r2(unsigned int r1, unsigned int r2){
        for (unsigned int j = 0; j < cols; j++) {
            data(r1*cols + j) += data(r2*cols + j);
    }
    }

    template<typename T>
    void Matrix<T>::mr1_r2(unsigned int r1, unsigned int r2){
        for (unsigned int j = 0; j < cols; j++) {
            data(r1*cols + j) -= data(r2*cols + j);
    }
    }

    template<typename T>
    void Matrix<T>::mr_a(unsigned int r, T a){
        for (unsigned int j = 0; j < cols; j++) {
            data(r*cols + j) *= a;
    }
    }

    template<typename T>
    void Matrix<T>::print_m(){
        for (int i=0; i<rows; i++){
            for (int j=0; j<cols; j++){
            std::cout<<(*this)(i,j)<<" ";
            }
            std::cout<<" "<<std::endl;
        }
        std::cout<<" "<<std::endl;
    }

    template<typename T>
    T Matrix<T>::get_det(){
        Matrix<T> copy = *this;
        double cof = 1;
        for (unsigned int i = 0; i<rows; i++){
            for (unsigned int j = i+1; j<rows ;j++){
                if (copy(i,i)==0){
                    for (unsigned int g = i+1; g<rows; g++){
                        if (copy(g,i)!=0){
                            copy.change_row(g, i);
                            break;
                        }
                    }
                }
                if (copy(i,i)!=0 and copy(j,i)!=0){
                copy.print_m();
                cof = cof * (copy(i,i)/copy(j,i));
                copy.mr_a(i, copy(j,i)/copy(i,i));

                copy.mr1_r2(j,i);
                }
            }
        } 
        T d = 1;
        for (unsigned int i = 0; i<rows; i++)
            d*= copy(i,i);
        return d*cof;
    }