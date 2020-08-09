//a tree can be deleted in post order way 

#include<iostream>
#include<queue>
using namespace std;

struct Node 
{
    int key;
    Node *left, *right;

    Node(int key) {
        this -> key = key;
        this -> left = this -> right = nullptr;
    }
};

void deleteTree(Node * &node) {
    if (node == nullptr) {
        return;
    }
    deleteTree(node -> left);
    deleteTree(node -> right);

    delete node;

    node = nullptr;
}

void deleteTreeRecursive(Node * &node) {
if (node == nullptr) {
        return;
    }
    queue<Node*> q;
    q.push(node);
    Node *front;
    while(!q.empty()) {
        front = q.front();
        q.pop();
        if (front -> left) {
            q.push(front -> left);
        }
        if (front -> right) {
            q.push(front -> right);
        }

    delete front;
    }
    node = nullptr;

}

int main() {
    Node* root = nullptr;

	root = new Node(15);
	root->left = new Node(10);
	root->right = new Node(20);
	root->left->left = new Node(8);
	root->left->right = new Node(12);
	root->right->left = new Node(16);
	root->right->right = new Node(25);

	// delete entire tree
	deleteTreeRecursive(root);

	if (root == nullptr)
		cout << "Tree Successfully Deleted" << endl;

	return 0;
}