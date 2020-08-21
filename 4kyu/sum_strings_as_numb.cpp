#include <string>
#include <iostream>
std::string sum_strings(const std::string& a, const std::string& b) {
  std::cout << a << " " << b << std::endl;
  return std::to_string(std::stoi(a) + std::stoi(b));
}
int main() {
    std::string a = "123" , b = "456";
    std::cout << sum_strings(a, b) << std::endl;

}
