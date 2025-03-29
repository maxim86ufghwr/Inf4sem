#include <iostream>
#include "/home/maxivanov/test/lab/Nzerprodv/src/vector.hpp"
#include "/home/maxivanov/test/lab/Nzerprodv/src/matrix.hpp"
#include <random>
#include <chrono>


int rand_uns(int min, int max)
{       unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
        static std::default_random_engine e(seed);
        std::uniform_int_distribution<int> d(min, max);
        return d(e);}

namespace matr {
    unsigned int n = 10;
    Matrix<int> m{n, n, 1};
}


int main()
{
int h = rand_uns(1, 10);

Matrix<int> m3 = Matrix<int>::getSpecificDeterminant(matr::n, h);

if (h != m3.get_det()){
    std::cout << "!!! fault determenant test: \t\t" << std::endl;
    return 0;
}

std::cout << "003 test determenant" << std::endl;

return 0;
}