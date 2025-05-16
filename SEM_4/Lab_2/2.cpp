#include <iostream>
#include <tuple>
#include <utility>

template <std::size_t Index = 0, typename... Tuplet>
typename std::enable_if<Index == sizeof...(Tuplet), std::ostream&>::type
printTuple(std::ostream& os, const std::tuple<Tuplet...>&) {
    return os;
}

template <std::size_t Index = 0, typename... Tuplet>
typename std::enable_if<Index < sizeof...(Tuplet), std::ostream&>::type
printTuple(std::ostream& os, const std::tuple<Tuplet...>& t) {
    os << std::get<Index>(t) << ' ';
    return printTuple<Index + 1>(os, t);
}


template<typename ... elem_t>
std::ostream& operator<<(std::ostream& os, std::tuple<elem_t...> t) {
    return printTuple(os, t);
}

int main() {
    int r = 3;
    const char* e = "r";
    std::tuple<int, double, int, int, const char*> t  = std::make_tuple(1, 2.4, r, 22, e);
    std::cout << t;
}