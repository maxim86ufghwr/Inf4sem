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
    unsigned int n = 100;
    Matrix<int> m{n, n, 1};
}

int main()
{
    for (int i = 0; i < matr::n; i++)
    {
        for (int j = 0; j < matr::n; j++)
        {
            matr::m(i,j) = rand_uns(1, 10);
        }
    }
    matr::m.transpose();
    Matrix<int> m_t = matr::m;
    matr::m.transpose();
    for (int i = 0; i < matr::n; i++) {
    for (int j = 0; j < matr::n; j++) {
    if (matr::m(i, j) != m_t(j, i))
    {
        std::cout <<"--- !!! Failed transponse !!! ---" << std::endl;
        return 0;
    }
    }
    }
    std::cout << "001 Transponse test: \t\t\t" << std::endl;
    return 0;
}