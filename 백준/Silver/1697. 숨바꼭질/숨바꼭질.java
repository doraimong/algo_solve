import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

class Pair{
	int location, sec;

	public Pair(int location, int sec) {
		super();
		this.location = location;
		this.sec = sec;
	}
}

public class Main {
	
	static int N, K;
	static boolean[] visit;
	
	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(in.readLine());
		visit = new boolean[100001];
		
		N = Integer.parseInt(st.nextToken()); 
		K = Integer.parseInt(st.nextToken());
		
		visit[N] = true;
		
		Queue<Pair> q = new ArrayDeque<>();
		
		q.offer(new Pair(N , 0));
		
		while(!q.isEmpty()) {
			int location = q.peek().location;
			int sec = q.peek().sec;
			
			visit[location]=true;
			
			if(location == K) {
				System.out.println(sec);
				break;
			}
			
			q.poll();
			
			int nextLocation = location-1;
			if(-1 < nextLocation && nextLocation < 100001 && !visit[nextLocation]) {
				visit[nextLocation] = true;
				q.offer(new Pair(nextLocation,sec+1));
			}
			
			nextLocation = location+1;
			if(-1 < nextLocation && nextLocation < 100001 && !visit[nextLocation]) {
				visit[nextLocation] = true;
				q.offer(new Pair(nextLocation,sec+1));
			}
			
			nextLocation =  2*location;
			if(-1 < nextLocation && nextLocation < 100001 && !visit[nextLocation]) {
				visit[nextLocation] = true;
				q.offer(new Pair(nextLocation,sec+1));
			}
		}
		
		
		
	}
}