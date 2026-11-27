#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <iterator>
#include <random>
#include <sstream>
#include <vector>
using namespace std;

const int limit = 1 << 20;
const int prefix = limit / 4;
using Pair = array<int, 2>;

vector<int> read_points(istream& input) {
    string str((istreambuf_iterator<char>(input)), {});
    for (char& ch : str) if (ch < '0' || ch > '9') ch = ' ';
    istringstream numbers(str);
    vector<int> points;
    for (int x; numbers >> x;) points.push_back(x);
    return points;
}

vector<int> improve(const vector<int>& points, mt19937& rng) {
    vector<Pair> owners(limit+1, {-1,-1});
    vector<int> index(limit+1, -1);
    for (int i=0; i<(int)points.size(); ++i) {
        index[points[i]] = i;
        for (int j=0; j<i; ++j)
            owners[points[i]-points[j]] = {i,j};
    }
    vector<vector<int>> lists(points.size());
    vector<int> free_points;
    for (int x=prefix+1; x<=limit; ++x) {
        if (index[x]>=0) continue;
        bool changed=false;
        vector<int> blockers;
        // For each collision, at least one of its existing points must go.
        auto require = [&](int i,int j,int k) {
            if (!changed) {
                changed=true;
                for (int v : {i,j,k})
                    if (v>=0 && points[v]>prefix && find(blockers.begin(),blockers.end(),v)==blockers.end())
                        blockers.push_back(v);
            } else {
                erase_if(blockers,[&](int v){return v!=i && v!=j && v!=k;});
            }
        };
        for (int i=0; i<(int)points.size(); ++i) {
            int a=points[i];
            auto pair=owners[abs(x-a)];
            if (pair[0]>=0) require(i,pair[0],pair[1]);
            if (changed && blockers.empty()) break;
            int mirror=2*x-a;
            if (mirror>a && mirror<=limit && index[mirror]>=0)
                require(i,index[mirror],-1);
            if (changed && blockers.empty()) break;
        }
        if (!changed) free_points.push_back(x);
        for (int v : blockers) lists[v].push_back(x);
    }
    vector<int> best=points;
    for (int i=0; i<(int)points.size(); ++i) {
        if (points[i]<=prefix) continue;
        vector<int> pool=lists[i];
        pool.insert(pool.end(), free_points.begin(),free_points.end());
        if (pool.size()<2) continue;
        vector<int> base=points;
        base.erase(base.begin()+i);
        vector<bool> used(limit+1);
        for (size_t a=0; a<base.size(); ++a)
            for (size_t b=0; b<a; ++b) used[base[a]-base[b]]=true;
        for (int attempt=0; attempt<3; ++attempt) {
            shuffle(pool.begin(),pool.end(),rng);
            auto chosen=base;
            auto occupied=used;
            for (int x : pool) {
                vector<int> gaps;
                bool good=true;
                for (int a : chosen) {
                    int gap=abs(x-a);
                    if (occupied[gap]) { good=false; break; }
                    occupied[gap]=true;
                    gaps.push_back(gap);
                }
                if (good) chosen.push_back(x);
                else for (int gap:gaps) occupied[gap]=false;
            }
            if (chosen.size()>best.size()) best=chosen;
        }
    }
    sort(best.begin(),best.end());
    return best;
}

int main() {
    auto points = read_points(cin);
    mt19937 rng(39);
    for (int round=0; round<16; ++round) {
        auto next=improve(points,rng);
        if (next.size()==points.size()) break;
        points=next;
        cerr << "size " << points.size() << endl;
    }
    cout << "[";
    for (size_t i=0;i<points.size();++i) cout << (i?",":"") << points[i];
    cout << "]\n";
}
