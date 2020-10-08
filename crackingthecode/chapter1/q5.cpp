// Cracking the code 1.5 One Away

// This could use a refactor
#include <iostream>
#include <string>
#include <cstdlib>
#include <cassert>

using namespace std;

bool isOneAway(string s1, string s2) {

    int diff = abs(int(s1.length() - s2.length()));
    bool allEqual = true;
    if (diff > 1) {
        return false;
    } else if (diff == 0) {
        int j = 0;
        for (int i = 0; i < s1.length(); i++) {
            if(s1[i] != s2[j]) {
                if (!allEqual) {
                    return false;
                }
                allEqual = false;
            }
            j++;
        }
    } else {
        int maxLength = max(int(s1.length()), int(s2.length()));
        int j = 0;
        for (int i = 0; i < maxLength; i++) {
            if(s1[i] != s2[j]) {
                if (!allEqual) {
                    return false;
                }
                if (s1.length() > s2.length()) {
                    j--;
                } else {
                    i--;
                }
                allEqual = false;
            }
            j++;
        }
    }
    
    return true;
}

int main() {
    // Testing
    assert(isOneAway("abc", "abb"));
    assert(isOneAway("abc", "abb"));
    assert(isOneAway("abcd", "abc"));
    assert(isOneAway("abcxy", "abxy"));
    assert(isOneAway("abxyz", "abxy"));
    assert(isOneAway("abyax", "abdyax"));
    assert(!isOneAway("abxyz", "abzz"));
    return 0;
}