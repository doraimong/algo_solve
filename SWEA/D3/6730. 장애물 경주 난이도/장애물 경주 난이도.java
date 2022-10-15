import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws Exception {

		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int T;
		T = Integer.parseInt(in.readLine());
		///////////////////////////////////////////////////////////////////////
		for (int test_case = 1; test_case <= T; test_case++) {

			int total = Integer.parseInt(in.readLine());
			
			int[] arr = new int[total];
			
			StringTokenizer st = new StringTokenizer(in.readLine());
			for(int i=0; i<total; i++)arr[i] = Integer.parseInt(st.nextToken());
			
			int up=0, down=0;
			for(int i=0; i<total-1; i++) {
				if(arr[i] < arr[i+1]) {
					up = Math.max(up, arr[i+1]-arr[i]);
				} else if(arr[i] > arr[i+1]) {
					down = Math.max(down, arr[i]-arr[i+1]);
				}
			}
			
			System.out.println("#"+test_case+" "+up+" "+down);

			///////////////////////////////////////////////////////////
		}
	}
	
}
