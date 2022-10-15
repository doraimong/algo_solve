import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int daysInMonth[] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	
	public static void main(String[] args) throws Exception {

	//	System.setIn(new FileInputStream("input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int T;
		T = Integer.parseInt(in.readLine());
		///////////////////////////////////////////////////////////////////////
		for (int test_case = 1; test_case <= T; test_case++) {

			StringTokenizer st = new StringTokenizer(in.readLine());

			int m,d;
			m = Integer.parseInt(st.nextToken());
			d = Integer.parseInt(st.nextToken());
			
			int dayOfWeek = 4;	//1월1일의 요일
			
			for(int i=0; i<m-1; i++) {//m-1 개월 계산
				dayOfWeek+=daysInMonth[i];
			}
			
			dayOfWeek += d-1;	//d-1 일 계산
			
			dayOfWeek %= 7;		//요일 계산
			
			System.out.println("#"+test_case+" "+dayOfWeek);

			///////////////////////////////////////////////////////////
		}
	}
	
}
