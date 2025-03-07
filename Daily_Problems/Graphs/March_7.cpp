// https://www.geeksforgeeks.org/problems/topological-sort/1
class Solution {
    public:
      vector<int> topologicalSort(vector<vector<int>>& adj) {
          int m= adj.size();
          vector<int> res;
          vector<int>mpp(m,0);
          queue<int>q;
          for(int i=0;i<m;i++){
              int n=adj[i].size();
              for(int j=0;j<n;j++){
                  mpp[adj[i][j]]+=1;
              }
          }
          for(int i=0;i<m;i++){
              if(mpp[i]==0){
                  q.push(i);
              }
          }
          while(!q.empty()){
              int index=q.front();
              res.push_back(index);
              q.pop();
              for(int x:adj[index]){
                  mpp[x]--;
                  if(mpp[x]==0){
                      q.push(x);
                  }
              }
          }
          return res;
      }
  };
// TC:O(M^2)
// SC:O(N)
// Approach: push the elements which occurs zero into the queue and decrease the degree of other elements