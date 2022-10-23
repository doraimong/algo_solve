/*
 * dp[i][w] : i개의 추로 w인 공의 무게를 확인 할 수 있는가
 * 유도 : 아무거도 않기, 추를 추가, 추 무게빼기
 */
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	
	static char res;
	static int chooCnt, chooArr[];
	static boolean dp[][];
	
	static void solve(int i, int w) {
		
		if(i > chooCnt || dp[i][w]) {
			return;
		}
		
		dp[i][w] = true;
		
		solve(i+1, w);
		solve(i+1, w+chooArr[i]);
		solve(i+1, Math.abs(w-chooArr[i]));
	}
	
	public static void main(String[] args) throws Exception {
	
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st; 
		
		chooCnt = Integer.parseInt(in.readLine());
		chooArr = new int[31];
		
		dp = new boolean[31][15001];
		
		st = new StringTokenizer(in.readLine());
		for(int i=0; i<chooCnt; i++)chooArr[i] = Integer.parseInt(st.nextToken());
		
		int ballCnt = Integer.parseInt(in.readLine());
		int[] ballArr = new int[ballCnt];
		
		solve(0, 0);
		
		st = new StringTokenizer(in.readLine());
		
		for(int i=0; i<ballCnt; i++) {
			int ballSize = Integer.parseInt(st.nextToken());
			if(ballSize > 15000)System.out.print("N ");
			else if(dp[chooCnt][ballSize])System.out.print("Y ");
			else System.out.print("N ");
		}
	}
}
