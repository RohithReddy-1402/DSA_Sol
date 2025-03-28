class Solution {
public:
    vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
        int n=grid.size();
        int m=grid[0].size();
        vector<vector<int>>q;
        for(int i=0;i<queries.size();i++){
            q.push_back({queries[i],i});
        }
        sort(q.begin(),q.end());
        vector<pair<int,int>>direction={{-1,0},{1,0},{0,1},{0,-1}};
        int totalCount=0;
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>pq;
        pq.push({grid[0][0],0});
        vector<vector<int>>vis(n,vector<int>(m,0));
        vis[0][0]=1;
        vector<int>ans(queries.size(),0);
        for(int i=0;i<q.size();i++){
            int value=q[i][0];
            int index=q[i][1];
            while(pq.size()&&pq.top().first<value){
                auto [node,xy]=pq.top();
                pq.pop();
                int x=xy/m;
                int y=xy%m;
                totalCount++;
                for(auto &it:direction){
                    int nx=x+it.first;
                    int ny=y+it.second;
                    if(nx>=0&&ny>=0&&nx<n&&ny<m&&vis[nx][ny]==0){
                        pq.push({grid[nx][ny],nx*m+ny});
                        vis[nx][ny]=1;
                    }
                }
            }
            ans[index]=totalCount;
        }
        return ans;
    }
};