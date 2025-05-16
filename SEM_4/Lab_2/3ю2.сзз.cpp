
#include <iostream>

template<int N, typename T, T... Coefficients>
struct LinearRecurrence {
    static constexpr T compute(int k) {
        if (k < N) {
            return initialValues[k];
        }

        T result = 0;
        int i = 0;
        ((result += Coefficients * compute(k - 1 - i++)), ...);
        
        return result;
    }

    static constexpr T initialValues[N] = {1, 1};
};

int main() {
    constexpr int k = 10;
    constexpr int result = LinearRecurrence<2, int, 1, 1>::compute(k);
    
    std::cout << result << std::endl;
    return 0;
}