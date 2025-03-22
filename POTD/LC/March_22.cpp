class Solution {
    public:
        
    
        int countCompleteComponents(int n, vector<vector<int>>& edges) {
            vector<vector<int>> adj(n);  
            vector<int> vis(n, 0);  
    
            for(auto& edge : edges) {
                int start = edge[0];
                int end = edge[1];
                adj[start].push_back(end);
                adj[end].push_back(start);
            }
    
            int count = 0;
    
            for (int i = 0; i < n; i++) {
                if (!vis[i]) {
                    vector<int> component;
                    queue<int> q;
                    q.push(i);
                    vis[i] = 1;
    
                    while (!q.empty()) {
                        int node = q.front();
                        q.pop();
                        component.push_back(node);
    
                        for (int neighbor : adj[node]) {
                            if (!vis[neighbor]) {
                                vis[neighbor] = 1;
                                q.push(neighbor);
                            }
                        }
                    }
    
                    bool isComplete = true;
                    int size = component.size();
                    for (int node : component) {
                        if (adj[node].size() != size - 1) {
                            isComplete = false;
                            break;
                        }
                    }
    
                    if (isComplete) count++;
                }
            }
            return count;
        }
    };
    