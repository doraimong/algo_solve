import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

class Pair{
	int r,c;

	public Pair(int r, int c) {
		this.r = r;
		this.c = c;
	}

	@Override
	public String toString() {
		return "Pair [r=" + r + ", c=" + c + "]";
	}
}

public class Main { 
	
	static int N,M, max, ee=0;
	static int[][] map;
	static int[][] tempMap;
	static int[] pick;
	static List<Pair> zeroLocation;
	static List<Pair> virusLocation;
	
	static int dr[] = {0, 0, 1, -1};
	static int dc[] = {1, -1, 0, 0};
	
	static void spread() {
		Queue<Pair> queue = new ArrayDeque<>();
		for(int i=0; i<virusLocation.size(); i++) {
			int r = virusLocation.get(i).r;
			int c = virusLocation.get(i).c;
			queue.offer(new Pair(r, c));
		}
		
		while(!queue.isEmpty()) {
			Pair pair = queue.poll();
			
			for(int i=0; i<4; i++) {
				int tempR = pair.r + dr[i];
				int tempC = pair.c + dc[i];
				
				if(0<= tempR && tempR<N && 0<= tempC && tempC<M 
						&& tempMap[tempR][tempC]==0) {
					tempMap[tempR][tempC] = 2;
					queue.offer(new Pair(tempR, tempC));
				}
			}
		}
		
	}
	
	static int countSafe() {
		int cnt=0;
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(tempMap[i][j] == 0)cnt++;
			}
		}
		
		return cnt;
	}
	
	static void perm(int start, int cnt) {
		if(cnt == 3) {
			for(int i = 0; i<N; i++) {
				for(int j=0; j<M; j++) {
					tempMap[i][j] = map[i][j];
				}
			}
			spread();
			int getCnt = countSafe();
			max = Math.max(max, getCnt);
			return;
		}
		
		for(int i=start; i<zeroLocation.size(); i++) {
			pick[cnt]=i;
			map[zeroLocation.get(i).r][zeroLocation.get(i).c]=1;
			perm(i+1, cnt+1);
			map[zeroLocation.get(i).r][zeroLocation.get(i).c]=0;
		}
	}
	
	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(in.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		map = new int[N][M];
		tempMap = new int[N][M];
		pick = new int[3];
		max = Integer.MIN_VALUE;
		
		zeroLocation = new ArrayList<>();
		virusLocation = new ArrayList<>();
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(in.readLine());
			for(int j=0; j<M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if(map[i][j] == 0)zeroLocation.add(new Pair(i,j));
				else if(map[i][j] == 2) virusLocation.add(new Pair(i, j));
			}
		}
		
		perm(0, 0);
		
		System.out.println(max);
	}
}