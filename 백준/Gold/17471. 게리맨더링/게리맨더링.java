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
		super();
		this.r = r;
		this.c = c;
	}
}

public class Main { 
	
	static int total, resMin, cnt;
	static boolean[] pick;	//1 시작 index == spot
	static int[] arr;	//1 시작 - 선거구 인구
	static boolean[][] conn;	//1 시작 index == spot
	
	
	static void perm(int start, int cnt, int max) {	//시작점, 뽑은 개수, 뽑을 전체 개수
		if(cnt == max) {
			List<Integer> pick1, pick2;			// index != spot
			pick1 = new ArrayList<Integer>();	//0index = 1정점 
			pick2 = new ArrayList<Integer>();
			for(int i=1; i<=total; i++) {
				if(pick[i]==true)pick1.add(i);
				else pick2.add(i);
			}
			
			//연결되었는지 (두개 선거구) -> ok -> 인구확인
			if(isConnected(pick1) && isConnected(pick2)) {
				int population1=0, population2=0;
				
				for(int i=0; i<pick1.size(); i++) {
					population1 += arr[pick1.get(i)];
				}
				for(int i=0; i<pick2.size(); i++) {
					population2 += arr[pick2.get(i)];
				}
				
			    resMin = Math.min(resMin, Math.abs(population1 - population2));
			}
			
			return ;
		}
		
		for(int i=start; i<=total; i++) {
			pick[i] = true;	//pick 1~6 마킹 true
			perm(i+1, cnt+1, max);
			pick[i] = false;
		}
	}
	
	static boolean isConnected(List<Integer> pick) {
		//bfs탐색
		Queue<Integer> queue = new ArrayDeque<>();
		boolean[] visit = new boolean[total+1];//1시작 index == spot
		int checkCnt = 0;
		int spot = pick.get(0);	//정점 번호
		
		queue.offer(spot);
		visit[spot] = true;
		checkCnt++;
		
		while(!queue.isEmpty()) {
			spot = queue.poll();
			for(int i=1; i<=total; i++) {//간선 정보 
				if(conn[spot][i] && pick.contains(i) && !visit[i]) {	//연결되어있고, 같은 선거구이고, 미방문지 라면
					visit[i] = true;
					checkCnt++;
					queue.offer(i);
				}
			}
		}
		//선거구 요소의 개수와 선택된 개수가 동일하다면 연결 완료return
		if(checkCnt == pick.size())return true;
		else return false;
		
	}
	
	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		total = Integer.parseInt(in.readLine());
		resMin = Integer.MAX_VALUE;
		
		arr = new int[total+1];
		pick = new boolean[total+1];
		conn = new boolean[total+1][total+1];
		
		st = new StringTokenizer(in.readLine());
		for(int i=1; i<=total; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		//간선정보
		for(int i=1; i<=total; i++) {
			st = new StringTokenizer(in.readLine());
			int tempTotal = Integer.parseInt(st.nextToken());
			for(int j=0; j<tempTotal; j++) {
				int temp = Integer.parseInt(st.nextToken());
				conn[temp][i]=conn[i][temp]=true;
			}
		}
		cnt=0;
		for(int i=1; i<total/2+1; i++) {//뽑을 개수
			perm(1, 0, i);
		}
		
		if(resMin == Integer.MAX_VALUE)resMin=-1;
		
		System.out.println(resMin);
		
	}
}