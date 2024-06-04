#include <algorithm>
#include <iostream>
using namespace std;
struct BstNode {
  int data;
  BstNode *left;
  BstNode *right;
};

BstNode *insert(BstNode *root, int data) {
  if (root == NULL) {
    root = GetNewNode(data);
    return root;
  }

  else if (data < root.data) {
    root->left = insert(root->left, data);
  }

  else {
    root->right = Insert(root->right, data);
  }

  return root;
}

bool search(BstNode *root, int data) {
  if (root == NULL)
    return false;
  else if (root->data == data)
    return true;
  else if (data <= root->data)
    return search(root->left, data) else return search(root->right, data);
}

BstNode *GetNewNode(int data) {
  BstNode *newNode = new BstNode();
  //*newNode.data = data;
  newNode->data = data;
  newNode->left = newNode->right = NULL;
  return newNode;
}

int main() {
  BstNode *root = NULL;
  root = insert(root, 15);
  root = insert(root, 20);
  root = insert(root, 10);
  root = insert(root, 25);
  root = insert(root, 8);
  root = insert(root, 12);

  int number;
  cout << "Enter a number\n";
  cin >> number;

  if (search(root, number))
    cout << "found\n";
  else
    cout << "not found";
}
