#include <string>
class PrimeDecomp
{
public:
    static std::string factors(int num) {
      std::string output = "";

      if (num % 2 == 0) {
        output += removeFactors(num, 2);
      }

      int i = 3;
      while (num != 1) {
        if (num % i == 0) {
          output += removeFactors(num, i);
        }
        i += 2;
      }
      return output;
    }

    static std::string removeFactors(int &num, int factor) {
      std::string output = "(";
      output += std::to_string(factor);
      int power = 0;
      while (num % factor == 0) {
        num /= factor;
        power ++;
      }
      if (power > 1) {
        output += "**";
        output += std::to_string(power);
      }
      output += ")";
      return output;
    }

};

