// https://leetcode.com/problems/flood-fill/
class Solution {
    public:
        vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
            int m = image.size();
            int n = image[0].size();
            int prevColor = image[sr][sc];
            if (prevColor == color) return image;
    
            queue<pair<int, int>> q;
            q.push({sr, sc});
            image[sr][sc] = color; 
    
            int directionX[4] = {0, 1, 0, -1};
            int directionY[4] = {1, 0, -1, 0};
    
            while (!q.empty()) {
                int row = q.front().first;
                int col = q.front().second;
                q.pop();
    
                for (int i = 0; i < 4; i++) {
                    int newRow = row + directionX[i];
                    int newCol = col + directionY[i];
    
                    if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n && image[newRow][newCol] == prevColor) {
                        image[newRow][newCol] = color;
                        q.push({newRow, newCol});
                    }
                }
            }
            return image;
        }
    };
    // TC:O(m*n)
    // SC:O(m*n)
    // Approach:Using BFS tranverse and change the color