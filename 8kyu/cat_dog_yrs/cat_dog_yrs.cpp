#include <vector>

std::vector<int> humanYearsCatYearsDogYears(int hy) {
    int catYears = (hy < 2 ? 15: 15 + 9);
    int dogYears = catYears;
    catYears += (hy > 2 ? (hy-2)*4 : 0);
    dogYears += (hy > 2 ? (hy-2)*5 : 0);
    return {hy, catYears, dogYears};
}
