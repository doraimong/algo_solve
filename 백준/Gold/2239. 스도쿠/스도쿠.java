import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

class Pair{
	int r, c;

	public Pair(int r, int c) {
		this.r = r;
		this.c = c;
	}

	@Override
	public String toString() {
		return "Pair [r=" + r + ", c=" + c + "]\n";
	}
}

public class Main {

	static int[][] map;
	static boolean [][]row, col, matrix;
	static List<Pair> zeroLocation;
	
	static void fillMap(int cnt) {
		
		if(cnt == zeroLocation.size()) {
			for(int i=0; i<9; i++) {
				for(int j=0; j<9; j++) {
					System.out.print(map[i][j]);
				}System.out.println();
			}
			System.exit(0);
			return;
		}
        
		int r = zeroLocation.get(cnt).r;
		int c = zeroLocation.get(cnt).c;

		for(int i=1; i<=9; i++) {
			if(!matrix[r/3*3 + c/3][i] && !row[r][i] && !col[c][i]) {
				matrix[r/3*3 + c/3][i] = col[c][i] = row[r][i] = true;
				map[r][c] = i;
				fillMap(cnt+1);
				matrix[r/3*3 + c/3][i] = col[c][i] = row[r][i] = false;
				map[r][c] = 0;
			}
		}
	}
	
	public static void main(String[] args) throws Exception {

		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		map = new int[9][9];
		row = new boolean[9][10];
		col = new boolean[9][10];
		matrix = new boolean[9][10];
		zeroLocation = new ArrayList<>();
		
		for(int i=0; i<9; i++) {
			String s = in.readLine();
			for(int j=0; j<9; j++) {
				map[i][j] = s.charAt(j) - '0';
				if(map[i][j] == 0) {zeroLocation.add(new Pair(i, j));}
				else {
					matrix[i/3*3 + j/3][map[i][j]] = col[j][map[i][j]] = row[i][map[i][j]] = true;
				}
			}
		}
		
		fillMap(0);
		
	}
}