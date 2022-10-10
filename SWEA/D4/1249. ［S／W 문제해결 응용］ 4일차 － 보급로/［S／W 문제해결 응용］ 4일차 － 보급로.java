
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;


class Pair {
	int r,c, total;

	public Pair(int r, int c, int total) {
		this.r = r;
		this.c = c;
		this.total = total;
	}
}

public class Solution {
	
	static int size, min;
	static int [][] map, visit;
	static int dr[] = {0, 0, 1, -1};
	static int dc[] = {1, -1, 0, 0};
	
	static void bfs() {
		Queue<Pair> queue = new ArrayDeque<>();
		queue.offer(new Pair(0, 0, 0));
		visit[0][0]=0;
		min = Integer.MAX_VALUE;
		
		while(!queue.isEmpty()) {
			Pair pair = queue.poll();
			
			for(int i=0; i<4; i++) {
				int tempR = pair.r + dr[i], tempC= pair.c + dc[i];
				
				if(0<=tempR && tempR<size && 0<=tempC && tempC<size 
						&& pair.total + map[tempR][tempC] < visit[tempR][tempC]) {
					visit[tempR][tempC] = pair.total + map[tempR][tempC];
					queue.offer(new Pair(tempR, tempC, pair.total + map[tempR][tempC]));
				}
			}
		}
		
	}

	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(in.readLine());
		for(int test_case=1; test_case<=T; test_case++) 
		{
			size = Integer.parseInt(in.readLine());
			map = new int[size+1][size+1];
			visit = new int[size+1][size+1];
			for(int i=0; i<=size; i++)Arrays.fill(visit[i], Integer.MAX_VALUE);
			
			for(int i=0; i<size; i++) {
				String s = in.readLine();
				for(int j=0; j<size; j++) {
					map[i][j] = s.charAt(j) - '0';
				}
			}
			
			bfs();
			System.out.println("#"+test_case+" "+visit[size-1][size-1]);
		}
	}
}