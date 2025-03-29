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

if (matr::m.get_rows() != matr::n or matr::m.get_cols() != matr::n)
{
    std::cout <<"--- !!! Failed get !!! ---" << std::endl;
    return 0;
}

Matrix<int> m_ch = matr::m;

for (int i; i < matr::n ; i++)
{
    m_ch.change_row(i, i+1);
    for (int j; j < matr::n ; j++){
        if (matr::m(1, j) != m_ch(i+1, j))
        {
        std::cout <<"--- !!! Failed change !!! ---" << std::endl;
        return 0;
        }
    }
}

for (int i; i < matr::n ; i++)
{
    m_ch.change_col(i, i+1);
    for (int j; j < matr::n ; j++){
        if (matr::m(j, 1) != m_ch(j, i+1))
        {
        std::cout <<"--- !!! Failed change !!! ---" << std::endl;
        return 0;
        }
    }
}

std::cout << "002 get and change test: \t\t" << std::endl;

return 0;
}