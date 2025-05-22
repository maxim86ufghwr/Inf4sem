#include <iostream>
#include <cstdlib>
#include "matrix.hpp"
#include "vector.hpp"


Matrix::Matrix(unsigned rows, unsigned cols, double value) : rows(rows), cols(cols) {
    data.resize(rows * cols);
    for (int i = 0; i < rows * cols; i++){
    data.push_back(value);}
}


Matrix Matrix::Identity(unsigned rows, unsigned cols){
    Matrix E{rows, cols};
    for (int j = 0; j < rows; j++)
        E(j, j) = 1;
    return E;
    }

Matrix Matrix::Zero(unsigned rows, unsigned cols){
    Matrix Z{rows, cols};
    return Z;
    }



Matrix Matrix::getSpecificDeterminant(unsigned n, double determinant){
        Matrix m = Matrix::Identity(n, n);
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
    
    unsigned int Matrix::get_rows() const { return rows; }
    
    unsigned int Matrix::get_cols() const { return cols; }

	// ... любые "getters", которые вам удобны ... //

    
	double& Matrix::operator()(unsigned row, unsigned col) {
        return data(row * rows + col);
    }
    
	double Matrix::operator()(unsigned row, unsigned col) const{
        return data(row * rows + col);
    }

    
    Matrix& Matrix::transpose(){
        for (unsigned int i = 0; i < rows; i++) {
            for (unsigned int j = 0; j < i; j++) {
                double c = data(j * cols + i);
                std::cout<<data(j * cols + i) << "/" << data(i * rows + j) <<"<-get"<<std::endl;
                data(j * cols + i) = data(i * rows + j);
                data(i * rows + j) = c;
            }
        }
    return *this;
    }

    
    Matrix Matrix::transpose() const {
        Matrix transposed{cols, rows};
        for (unsigned int i = 0; i < rows; i++) {
            for (unsigned int j = 0; j < cols; j++) {
                transposed(i*rows, j) = data(j*cols + i);
            }
        }
        return transposed;
    }

    
    void Matrix::change_row(unsigned int r1, unsigned int r2){
        for (unsigned int j = 0; j < cols; j++) {
            double c = data(r1*cols + j);
            data(r1*cols + j) = data(r2*cols + j);
            data(r2*cols + j) = c;
    }
    }

    
    void Matrix::change_col(unsigned int c1, unsigned int c2){
        for (unsigned int i = 0; i < rows; i++) {
            double c = data(i*cols + c1);
            data(i*cols + c1) = data(c2*cols + c2);
            data(i*cols + c2) = c;
    }
    }

    
    void Matrix::sr1_r2(unsigned int r1, unsigned int r2){
        for (unsigned int j = 0; j < cols; j++) {
            data(r1*cols + j) += data(r2*cols + j);
    }
    }

    
    void Matrix::mr1_r2(unsigned int r1, unsigned int r2){
        for (unsigned int j = 0; j < cols; j++) {
            data(r1*cols + j) -= data(r2*cols + j);
    }
    }

    
    void Matrix::mr_a(unsigned int r, double a){
        for (unsigned int j = 0; j < cols; j++) {
            data(r*cols + j) *= a;
    }
    }

    
    void Matrix::print_m(){
        for (int i=0; i<rows; i++){
            for (int j=0; j<cols; j++){
            std::cout<<(*this)(i,j)<<" ";
            }
            std::cout<<" "<<std::endl;
        }
        std::cout<<" "<<std::endl;
    }

    
    double Matrix::get_det(){
        Matrix copy = *this;
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
        double d = 1;
        for (unsigned int i = 0; i<rows; i++)
            d*= copy(i,i);
        return d*cof;
    }