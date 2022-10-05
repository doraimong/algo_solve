import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

class Model{
	int r,c,dis,key;

	public Model(int r, int c, int dis, int key) {
		this.r = r;
		this.c = c;
		this.dis = dis;
		this.key = key;
	}

	@Override
	public String toString() {
		return "Model [r=" + r + ", c=" + c + ", dis=" + dis + ", key=" + key + "]";
	}
	
}

public class Main { 
	
	static int N, M, startR, startC, min;
	static char[][] map;
	static boolean[][][] visit;
	static int dr[] = {0, 0, -1, 1};
	static int dc[] = {-1, 1, 0, 0};
	
	static void bfs() {
		Queue<Model> queue = new ArrayDeque<>();
		
		queue.offer(new Model(startR, startC, 0, 0));
		
		while(!queue.isEmpty()) {
			Model model = queue.poll();
			
		//	System.out.println(model.toString());
			
			if(map[model.r][model.c] == '1') {
				min = Math.min(min, model.dis);
				return;
			}
			
			for(int i=0; i<4; i++) {
				int nr = model.r + dr[i], nc = model.c + dc[i], dis = model.dis, key = model.key;
				if(0<=nr && nr<N && 0<=nc && nc<M  && map[nr][nc] != '#' && !visit[nr][nc][key]) {
					if(map[nr][nc] == '0' ||  map[nr][nc] == '.') {
						visit[nr][nc][key]=true;
						queue.offer(new Model(nr, nc, dis+1, key));
					} 
					else if(map[nr][nc] == '1') {
						visit[nr][nc][key]=true;
						
						queue.offer(new Model(nr, nc, dis+1, key));
					} 
					else if('a' <= map[nr][nc] && map[nr][nc] <= 'z') {
						key = key | 1 << (map[nr][nc] - 'a');
						visit[nr][nc][key]=true;
						queue.offer(new Model(nr, nc, dis+1, key));
					} 
					else if('A' <= map[nr][nc] && map[nr][nc] <= 'Z') {
						//비트마스킹 확인 후 통과
						int door = 1 << (map[nr][nc] - 'A');
						if((key & door) > 0) {
							visit[nr][nc][key]=true;
							queue.offer(new Model(nr, nc, dis+1, key));
						}
					}
				}
			}
		}
		
		//return -1;
	}
	
	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		min = Integer.MAX_VALUE;
		
		map = new char[N][M];
		visit = new boolean[N][M][65];
		
		for(int i=0; i<N; i++) {
			String s = in.readLine();
			for(int j=0; j<M; j++) {
				map[i][j] = s.charAt(j);
				if(map[i][j] == '0') {startR = i; startC = j;}
			}
		}
		
		bfs();
		if(min == Integer.MAX_VALUE)min = -1;
		System.out.println(min);
	}
}