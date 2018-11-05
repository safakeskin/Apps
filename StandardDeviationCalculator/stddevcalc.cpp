#include <iostream>
#include <cmath>
#include <vector>

void inputTaker( int size, std::vector<double>& v ){
    double input;
    for (size_t i = 0; i < size; i++) {
        std::cout << "Enter data " << i+1 <<": ";
        std::cin >> input;
        v.push_back( input );
    }
}

double meanCalculator( std::vector<double>& v ){
    long double avg = 0;
    for ( auto &element : v )
        avg += element;
    avg = ( avg / v.size() );
    std::cout << "Mean is: " << avg << '\n';
    return (double)avg;
}

double stdDevCalculator( double avg, std::vector<double>& v ){
    long double result = 0;
    for ( auto &element : v ) {
        result += pow((element - avg), 2 );
    }
    result /= v.size();
    return sqrt( result );
}

int main(int argc, char const *argv[]) {
    int size; double result;
    std::cout << "Enter size: "; std::cin >> size;
    std::vector<double> v;
    inputTaker( size, v);
    result = stdDevCalculator( (double)meanCalculator(v), v );
    std::cout << "Std. Dev.: " << result << '\n';
    return 0;
}
