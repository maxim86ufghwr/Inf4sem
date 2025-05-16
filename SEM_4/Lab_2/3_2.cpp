#include <iostream>
#include <array>

template<int N, typename T, T... Coefficients>
struct LinearRecurrence {
    static constexpr T compute(int k, const std::array<T, N>& initialValues) {
        if (k < N) {
            return initialValues[k];
        }
        
        T result = 0;
        int i = 0;
        ((result += Coefficients * compute(k - 1 - i++, initialValues)), ...);
        
        return result;
    }
};

int main() {
    constexpr int n = 2;
    constexpr std::array<int, n> initialValues = {1, 1}; 
    constexpr int k = 10;
    constexpr int result = LinearRecurrence<n, int, 1, 1>::compute(k, initialValues);
    
    std::cout << result << std::endl;
    return 0;
}