// https://leetcode.com/problems/campus-bikes/

#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>

class Solution {
 public:
  using triplet = std::tuple<int, int, int>;

  std::vector<int> assignBikes(const std::vector<std::vector<int>>& workers,
                               const std::vector<std::vector<int>>& bikes) {
    int nWorkers = workers.size();
    int nBikes = bikes.size();

    std::vector<int> assigned(nWorkers, -1);
    std::vector<int> used(nBikes, -1);

    std::vector<triplet> allDist;
    allDist.reserve(nWorkers * nBikes);

    for (int workerId = 0; workerId < nWorkers; ++workerId) {
      for (int bikeId = 0; bikeId < nBikes; ++bikeId) {
        int dist = std::abs(workers[workerId][0] - bikes[bikeId][0]) +
                   std::abs(workers[workerId][1] - bikes[bikeId][1]);
        allDist.push_back(std::make_tuple(dist, workerId, bikeId));
      }
    }

    // equal distance and equal worker id, sort by bike id
    // equal distance, sort by worker id
    // otherwise, sort by distance
    std::sort(allDist.begin(), allDist.end(),
              [](const triplet& a, const triplet& b) {
                if (std::get<0>(a) == std::get<0>(b)) {
                  if (std::get<1>(a) == std::get<1>(b)) {
                    return std::get<2>(a) < std::get<2>(b);
                  }
                  return std::get<1>(a) < std::get<1>(b);
                }
                return std::get<0>(a) < std::get<0>(b);
              });

    for (size_t ii = 0; ii < allDist.size(); ++ii) {
      if (assigned[std::get<1>(allDist[ii])] == -1 &&
          used[std::get<2>(allDist[ii])] == -1) {
        used[std::get<2>(allDist[ii])] = 1;
        assigned[std::get<1>(allDist[ii])] = std::get<2>(allDist[ii]);
      }
    }

    return assigned;
  }
};

void print_vec(const std::vector<int>& vec) {
  for (auto& v : vec) {
    std::cout << v << " ";
  }
  std::cout << std::endl;
}

int main(int argc, char** argv) {
  Solution s;
  std::vector<std::vector<int>> workers = {{0, 0}, {1, 1}, {2, 0}};
  std::vector<std::vector<int>> bikes = {{1, 0}, {2, 2}, {2, 1}};
  std::vector<int> assigned = s.assignBikes(workers, bikes);
  std::cout << "Assigned: ";
  print_vec(assigned);
  std::vector<int> expected = {0, 2, 1};
  std::cout << "Expected: ";
  print_vec(expected);
  return 0;
}