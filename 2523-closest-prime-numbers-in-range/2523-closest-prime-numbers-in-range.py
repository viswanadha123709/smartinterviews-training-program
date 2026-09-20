class Solution {
public:
    vector<int> closestPrimes(int left, int right) {

        vector<bool> isPrime(right + 1, true);

        isPrime[0] = false;
        isPrime[1] = false;

        for(int i = 2; i * i <= right; i++) {
            if(isPrime[i]) {
                for(int j = i * i; j <= right; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        vector<int> res;

        int minDiff = INT_MAX;

        for(int i = left; i <= right; i++) {

            if(isPrime[i]) {

                if(!res.empty()) {
                    minDiff = min(minDiff, i - res.back());
                }

                res.push_back(i);
            }
        }

        if(minDiff == INT_MAX)
            return {-1, -1};

        for(int i = 0; i < res.size() - 1; i++) {

            if(res[i + 1] - res[i] == minDiff) {
                return {res[i], res[i + 1]};
            }
        }

        return {-1, -1};
    }
};