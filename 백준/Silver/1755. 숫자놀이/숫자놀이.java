import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;


class Pair implements Comparable<Pair>{
	String s;
	int n;
	
	public Pair(String s, int n) {
		this.s = s;
		this.n = n;
	}

	@Override
	public int compareTo(Pair o) {
		return s.compareTo(o.s);
	}
	
}

public class Main {
	
	static String[] numToString = {"zero","one","two","three","four","five","six","seven","eight","nine"};
	
	public static void main(String[] args) throws Exception {
	
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		
		int start,end;
		start = Integer.parseInt(st.nextToken());
		end = Integer.parseInt(st.nextToken());
		
		List<Pair> arr = new ArrayList<>();
		
	
		for(int i=start; i<=end; i++) {
			String put = null;
			String temp = Integer.toString(i);
			for(int j=0; j<temp.length(); j++)put += numToString[temp.charAt(j) -'0'];
			arr.add(new Pair(put, i));
		}
		
		
		Collections.sort(arr);
		
		for(int i=0; i<arr.size(); i++) {
			System.out.print(arr.get(i).n + " ");
			if((i+1)%10 == 0)System.out.println();
		}
		
	}
}
