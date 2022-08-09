package medium._207;


// DFS
// detect any cycle in the graph
public class Solution {
    public boolean canFinish(int numCourse, int[][] prerequisites) {
        if (prerequisites.length ==0 ) {
            return true;
        }

        boolean[] visited = new boolean[numCourse];
        for (int i =0; i < numCourse; i ++) {
            boolean[] recStack = new boolean[numCourse];
            if (isCyclic(i, prerequisites, visited, recStack)) {
                return false;
            }
        }

        return true;
    }


    private boolean isCyclic(int v, int[][] prerequisites, boolean[] visited, boolean[] recStack) {
        if (recStack[v]) {
            return true;
        }

        if (visited[v]) {
            return false;
        }

        recStack[v] = true;
        visited[v] = true;
        for (int i =0; i < prerequisites.length; i ++) {
            if (v == prerequisites[i][1]) {
                int next = prerequisites[i][0];
                if (isCyclic(next, prerequisites, visited, recStack)) {
                    return true;
                }
            }
        }

        recStack[v] = false;
        return false;

    }
}
