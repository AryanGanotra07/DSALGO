vector<int> arr[100001];
vector<int> vis(100001);
int res;

int dfs(int v){
    vis[v]=1;
    
    int tree_count=0;
    for(int child: arr[v]){
        if(vis[child]==0){
            int subtree_count=dfs(child);
            if(subtree_count%2==0) res++;
            else tree_count+=subtree_count;
        }
    }
    return tree_count+1;
}

int Solution::solve(int A, vector<vector<int> > &B) {
    for(int i=1; i<=A; i++){
        arr[i].clear();
        vis[i]=0;
    }
    
    for(int i=0; i<B.size(); i++){
        arr[B[i][0]].push_back(B[i][1]);
        arr[B[i][1]].push_back(B[i][0]);
    }
    
    res=0;
    dfs(1);
    return res;
}
