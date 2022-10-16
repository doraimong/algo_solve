import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N,M;
	static int[][] map, dp;
	static int[] dr = {0, 0, 1, -1};
	static int[] dc = {1, -1, 0, 0};
	
	static int dfs(int r, int c) {
		if(r == N-1 && c == M-1) {
			return 1;
		}
		if(dp[r][c] != -1)return dp[r][c];
		
		dp[r][c] = 0;
		for(int i=0; i<4; i++) {
			int nr = r + dr[i], nc = c + dc[i];
			if(0<=nr && nr<N && 0<=nc && nc<M && map[r][c] > map[nr][nc]) {
				dp[r][c] += dfs(nr, nc);
			}
		}
		
		return dp[r][c];
	}
	
	public static void main(String[] args) throws Exception {
	
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		map = new int[N+1][M+1];
		dp = new int[N+1][M+1];
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(in.readLine());
			for(int j=0; j<M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				dp[i][j] = -1;
			}
		}
		
		
		
		dfs(0,0);
        
		System.out.println(dp[0][0]);
	}

}
