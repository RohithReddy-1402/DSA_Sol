//
// Created by Rohith Reddy on 03-03-2025.
//

//Question is https://leetcode.com/problems/rotting-oranges/
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        queue<pair<int,int>>q;
        int count=0,time=0,rotten=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]!=0)count++;
                if(grid[i][j]==2)q.push({i,j});
            }
        }
        int directionX[4]={0,1,0,-1};
        int directionY[4]={1,0,-1,0};
        while(!q.empty()){
            int k=q.size();
            rotten+=k;
            while(k--){
                int x=q.front().first;
                int y= q.front().second;
                q.pop();
                for(int i=0;i<4;i++){
                    int newX=x+directionX[i];
                    int newY=y+directionY[i];
                    if(newX<0||newY<0||newX>=m||newY>=n||grid[newX][newY]!=1)continue;
                    grid[newX][newY]=2;
                    q.push({newX,newY});
                }
            }
            if(!q.empty())time++;
        }
        return count==rotten?time:-1;
    }
};
// TC:O(M*N)
// SC:O(M*N)
// Approach:first loop through the grid and find the rotten tomatos then storing in the queue , Rotten the adjacent tomatos in 4 directions for every minute  using BFS