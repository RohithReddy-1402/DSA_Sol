
class Solution {
    public:
        vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
            unordered_map<string, vector<string>> graph;  
            unordered_map<string, int> in_degree;         
            
            for (string& recipe : recipes) {
                in_degree[recipe] = 0;
            }
            for (int i = 0; i < recipes.size(); i++) {
                for (string& ing : ingredients[i]) {
                    if (find(supplies.begin(), supplies.end(), ing) == supplies.end()) {
                        graph[ing].push_back(recipes[i]); 
                        in_degree[recipes[i]]++; 
                    }
                }
            }
            queue<string> q;
            for (string& recipe : recipes) {
                if (in_degree[recipe] == 0) {
                    q.push(recipe);
                }
            }
            vector<string> result;
            while (!q.empty()) {
                string recipe = q.front();
                q.pop();
                result.push_back(recipe);
                for (string& dependent : graph[recipe]) {
                    in_degree[dependent]--;
                    if (in_degree[dependent] == 0) {
                        q.push(dependent);
                    }
                }
            }
    
            return result;
        }
    };
    
// TC : O(N + M)
// SC : O(M + N) 
// Approch : Using the topological sorting we can solve this question 