// Given an m x n board of characters and a list of strings words, return all words on the board. 
//Each words must be constructed from the letters of teh sequentially adjacent cell, 
//where "adjacent" cells are those horizontally or vertically neighboring. 
//The same letter cell may not be used more than once in a word.

import java.util.*;

class AllWords {
    public static void main(String[] args) {
        char[][] board = {
            {'o', 'a', 'a', 'n'},
            {'e', 't', 'a', 'c'},
            {'i', 'h', 'k', 'r'},
            {'i', 'f', 'l', 'v'},

        };

        String[] words = {"oath", "pea", "eat", "rain"};
        System.out.println(findWords(board, words));;
    }

    public static String[] findWords(char[][] board, String[] words) {
        int m = board.length;
        int n = board[0].length;

        boolean[][] vis = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(vis[i], false);
        }

        for (int i = 0; i < board.length; i ++) {
            for (int j = 0; j < board[0].length; j++) {
                if (!vis[i][j]) {
                     dfs(board, vis, i, j, "", "");
                }
            }
        }
    }

    public
     static void dfs(char[][] board, boolean[][] vis, int i, int j, String word, List<String> result) {
        vis[i][j] = true;
        word += board[i][j];
        if (word.length() > 10) {
            return;
        }
        


    }
}