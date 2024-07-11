import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		// 결과를 한 번에 출력하기 위한 StringBuilder
		StringBuilder sb = new StringBuilder();

		StringTokenizer sub = new StringTokenizer(in.readLine(), "-");
		
		int temp=0;
		int[] num = new int[100];
		int cnt=0;
		while(sub.hasMoreTokens()) {
			StringTokenizer ad = new StringTokenizer(sub.nextToken(), "+");
			
			while(ad.hasMoreTokens()) {
				temp += Integer.parseInt(ad.nextToken());
			}
			
			num[cnt++] = temp;
			temp=0;
		}
		int res = num[0];
		for(int i=1; i<num.length; i++)res-=num[i];
		
		System.out.println(res);
		
	}
}