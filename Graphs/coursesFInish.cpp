#include<iostream>
using namespace std;


bool dfs(int i,vector<vector<int>> &adj,vector<bool> vis){

if(vis[i])
    return true;
    
vis[i]=true;

for(int j=0;j<adj[i].size();j++)
    if(dfs(adj[i][j],adj,vis))
        return true;
    
return false;
}

int Solution::solve(int A, vector<int> &B, vector<int> &C) {

vector<vector<int>> adj(A);

for(int i=0;i<B.size();i++)
    adj[B[i]-1].push_back(C[i]-1);
    
vector<bool> vis(A,false);

for(int i=0;i<A;i++)
    if(dfs(i,adj,vis))
        return 0;
return 1;
}