package hard._037_sudoku_solver;

import java.util.ArrayList;
import java.util.List;

public class Solution {

    public void solveSudoku(char[][] board) {
        int pos = 0;
        while (pos < 81 && board[pos / 9][pos % 9] != '.') {
            pos++;
        }

        char[][] result = new char[9][9];
        backtrack(board, pos/9, pos%9, result);

        for (int i=0; i < 9;i++)
            for (int j=0;j<9;j++) {
                board[i][j] = result[i][j];
            }

    }

    private void backtrack(char[][] board, int row, int col, char[][] result) {
        // what is end condition
        // if meet the End Condition
        if (row == 9 && col == 0) {
            for (int i=0; i < 9;i++)
                for (int j=0;j<9;j++) {
                    result[i][j] = board[i][j];
                }
            return;

        }

        List<Character> selections = selectionList(row, col, board);

        for (var c: selections) {
            board[row][col] = c;
            // how to skip number in here

            int nextPos = row * 9 + col + 1;
            while(nextPos<81 && board[nextPos / 9][nextPos % 9] != '.') {
                nextPos++;
            }
            backtrack(board, nextPos /9, nextPos % 9, result);
            board[row][col] = '.';
        }
    }

    private List<Character> selectionList(int row, int col, char[][] board) {
        ArrayList selections = new ArrayList<Character>();
        boolean[] existed = new boolean[9];
        // check row
        for (int i=0; i < 9; i++) {
            if (board[i][col] != '.') {
                char c = board[i][col];
                existed[c - '1'] = true;
            }
        }
        // check col
        for (int j=0; j < 9; j++) {
            if (board[row][j] != '.') {
                char c = board[row][j];
                existed[c - '1'] = true;
            }
        }
        // check region

        int lowerX = 3 * (row / 3);
        int upperX = lowerX + 3;

        int lowerY = 3 * (col / 3);
        int upperY = lowerY + 3;

        for (int i = lowerX; i < upperX; i++)
            for (int j = lowerY; j < upperY; j++) {
                if (board[i][j] != '.') {
                    char c = board[i][j];
                    existed[c - '1'] = true;
                }
            }

        // add non-existed number to selection list
        for (int k=0; k <9;k++) {
            if (existed[k] == false) {
                int index = k;
                selections.add((char) (index + '1'));
            }
        }

        return selections;
    }
}
