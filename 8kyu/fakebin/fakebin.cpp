// Fake Binary
// https://www.codewars.com/kata/57eae65a4321032ce000002d/

#include <iostream>
#include <string>
std::string fakeBin(std::string str){
    for (auto &c : str) c = (c - '0' < 5 ? '0' : '1');
    return str;
}

int main() {
    std::string s = "12123124123123696969696969567859678956789";
    std::cout << s << std::endl;
    s = fakeBin(s);
    std::cout << s << std::endl;
    return 0;
}
