class Solution {
    public:
        vector<int>parent;
        vector<int>cost;
        int find(int x){
            if(x==parent[x]) return x;
            return parent[x]=find(parent[x]);
        }
        void Union(int x,int y){
            parent[y]=x;
        }
        vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
            cost.assign(n,-1);
            parent.resize(n);
    
            for(int i=0;i<n;i++){
                parent[i]=i;
            }
    
            for(auto &vec:edges){
                int u=vec[0];
                int v=vec[1];
                int w=vec[2];
    
                int parent_u=find(u);
                int parent_v=find(v);
    
                if(parent_u!=parent_v){
                    cost[parent_u]&=cost[parent_v];
                    Union(parent_u,parent_v);
                }
    
                cost[parent_u]&=w;
            }
    
            vector<int>ans;
            for(auto &q:query){
                int s=q[0];
                int t=q[1];
                
                int p1=find(s);
                int p2=find(t);
                
                if(s==t) ans.push_back(0);
                else if(p1!=p2) ans.push_back(-1);
                else ans.push_back(cost[p1]);
            }
            return ans;
        }
    };
    // TC : O(N+E+Q)
    // SC : O(N)
    // Approach : classical DSU to find the edge between them and by applying and operation we get the minimum dist between nodes