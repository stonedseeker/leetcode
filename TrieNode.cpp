#include <algorithm>
#include <vector>
using namespace std;

struct TrieNode {
  TrieNode *childNode[26];

  bool wordEnd;

  TrieNode() {
    wordEnd = false;
    for (int i = 0; i < 26; i++) {
      childNode[i] = NULL
    }
  }
};

void insert_key(TrieNode *root, string &key) {
  TrieNode *currNode = root;

  for (auto c : key) {
    if (currNode->childNode[c - 'a'] == NULL) {
      TrieNode *newNode = new TrieNode();
      currNode->childNode[c - 'a'] = newNode;
    }

    currNode = currNode->childNode[c - 'a'];
  }

  currNode->wordEnd = 1;
}

bool search_key(TrieNode *root, string &key) {
  TrieNode *currNode = root;

  for (auto c : key) {
    if (currNode->childNode[c - 'a'] == NULL) {
      return false;
    }

    currNode = currNode->childNode[c - 'a'];
  }

  return (currNode->wordEnd == true);
}

int main() {
  TrieNode *root = new TrieNode();

  vector<string> inp = {"and", "ant", "do", "geek", "dad", "ball"};
  int n = inp.size();

  for (int i = 0; i < n; i++) {
    insert_key(root, inp[i]);
  }

  vector<string> searchQueryStrings = {"do", "geek", "bat"};

  // number of search operations in the Trie
  int searchQueries = searchQueryStrings.size();

  for (int i = 0; i < searchQueries; i++) {
    cout << "Query String: " << searchQueryStrings[i] << "\n";
    if (search_key(root, searchQueryStrings[i])) {
      // the queryString is present in the Trie
      cout << "The query string is present in the "
              "Trie\n";
    } else {
      // the queryString is not present in the Trie
      cout << "The query string is not present in "
              "the Trie\n";
    }
  }

  return 0;
}
