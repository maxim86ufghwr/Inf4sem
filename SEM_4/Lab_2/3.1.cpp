#include <iostream>

template<int... Values>
struct Split;

template<int First, int... Rest>
struct Split<First, Rest...> {
    static constexpr int element1 = First;
    using next = Split<Rest...>;
};

template<int Last>
struct Split<Last> {
    static constexpr int element1 = Last;
};

template<int N, int... Values>
struct SpecializationSelector;

template<int N, int First, int... Rest>
struct SpecializationSelector<N, First, Rest...> : public SpecializationSelector<N-1, Rest...> {
    static constexpr int value = First;
};

template<int First, int... Rest>
struct SpecializationSelector<0, First, Rest...> {
    static constexpr int value = First;
};

int main() {
    using SplitNumbers = Split<1, 2, 3, 4>;
    
    std::cout << SpecializationSelector<1, 1, 2, 3, 4>::element1 << std::endl; // 1
    std::cout << SpecializationSelector<0, 1, 2, 3, 4>::value << std::endl; // 1

    return 0;
}
