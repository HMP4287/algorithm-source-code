import java.util.*;
import java.io.*;

//2178
class Main {
    public static int[][] arr;
    public static boolean[][] visited;

    public static int bfs (int startX, int startY, int endX, int endY) {
        Queue<Node> q = new LinkedList<>();
        int[] dx = {-1, 0, 1, 0}; // 북 동 남 서
        int[] dy = {0, 1, 0, -1};

        visited[startX][startY] = true; // 방문 표시를 다음 위치에 해야되나 현재 위치에 해야되
        q.offer(new Node(startX, startY));
        while(!q.isEmpty()) {
            Node temp = q.poll();
            if(temp.x == endX-1 && temp.y ==endY-1)
                return arr[endX-1][endY-1];

            visited[temp.x][temp.y] = true;
            for (int i = 0; i < 4; i++) {
                if(temp.x+dx[i] < endX && temp.y+dy[i] < endY && temp.x+dx[i] >= 0 && temp.y+dy[i] >=0) {
                    if(!visited[temp.x + dx[i]][temp.y + dy[i]] && arr[temp.x + dx[i]][temp.y + dy[i]]==1) {
                        arr[temp.x + dx[i]][temp.y + dy[i]] = arr[temp.x][temp.y] + 1; // next int = previous int + 1
                        visited[temp.x + dx[i]][temp.y + dy[i]] = true;
                        q.offer(new Node(temp.x + dx[i], temp.y + dy[i]));
                    }
                }
            }
        }
        return arr[endX-1][endY-1];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        //bfs!
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String temp = br.readLine();
            for (int j = 0; j < m; j++)
                arr[i][j] = Integer.parseInt(String.valueOf(temp.charAt(j)));
        }

        bw.write(String.valueOf(bfs(0,0, n, m)));
        br.close();
        bw.flush();
        bw.close();
        br.close();
    }
}

class Node {
    int x,y;
    Node (int x, int y) {
        this.x = x;
        this.y = y;
    }
}
