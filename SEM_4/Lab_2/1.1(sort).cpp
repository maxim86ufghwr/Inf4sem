#include <iostream>
#include <vector>
#include <deque>
#include <chrono>
#include <iterator>
#include <functional>

template< typename RandomAccessIterator, typename Compare >
void sort( RandomAccessIterator first, RandomAccessIterator last, Compare comp);

template< typename RandomAccessIterator, typename Compare >
void sift_down(RandomAccessIterator first, RandomAccessIterator last, RandomAccessIterator ver, Compare comp){
    auto size = std::distance(first, ver) - 1;
while (ver + size + 1 <= last){
    RandomAccessIterator u = ver + size + 1;
    if (u + 1 <= last and comp(*(u + 1), *u)){
        u++;}
    if (comp(*u, *ver)){
        std::iter_swap(u, ver);
        ver = u;
    }
    else break;
}}

template< typename RandomAccessIterator, typename Compare >
void heapify(RandomAccessIterator first, RandomAccessIterator last, Compare comp){
for (auto it = last; it >= first; --it){
    sift_down(first, last, it, comp);
}}

template< typename RandomAccessIterator, typename Compare >
void extract_max(RandomAccessIterator first, RandomAccessIterator last, Compare comp){
    RandomAccessIterator last_c = last - 1;
    std::iter_swap(first, last_c);
    --last_c;
    sift_down(first, last_c, first, comp);
}

template< typename RandomAccessIterator, typename Compare >
void my_sort(RandomAccessIterator first, RandomAccessIterator last, Compare comp){
    auto size = std::distance(first, last);
    if (size < 1) {return;}
    RandomAccessIterator last_c = first + size;
    heapify(first, last, comp);
    for (auto it = last; it != first; --it){
        extract_max(first, it, comp);
        
    }
}


int main(){
    std::vector<int> vec = {5, 2, 9, 1, 5, 6, 45};
    std::deque<int> deq = {3, 7, 8, 5, 2, 4, 5};

    auto start = std::chrono::high_resolution_clock::now();
    my_sort(vec.begin(), vec.end(), std::greater<int>());
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> vec_time = end - start;
    std::cout<<"answer:"<<std::endl;
    for (auto it = vec.cbegin(); it != vec.cend(); ++it){
        std::cout<< *it <<" ";}
    
    std::cout<<std::endl;
    
    start = std::chrono::high_resolution_clock::now();
    my_sort(deq.begin(), deq.end(), std::greater<int>());
    end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> deq_time = end - start;
    std::cout<<"answer:"<<std::endl;
    for (auto it = deq.cbegin(); it != deq.cend(); ++it){
        std::cout<< *it <<" ";}
    
    
    std::cout<<std::endl;
    
    
    std::cout << "Время сортировки vector: " << vec_time.count() << " секунд\n";
    std::cout << "Время сортировки deque: " << deq_time.count() << " секунд\n";

    return 0;
}