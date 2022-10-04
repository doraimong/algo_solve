import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Stack;

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

	static int dr[] = {-1, 0, 1};
	static int dc[] = {1, 1, 1};
	static int R,C,res,state;
	static char map[][];
	static boolean visit[][];

	static boolean inMap(int r, int c) {
		if(-1<r && r<R && -1<c && c<C)return true;
		else return false;
	}


	static void dfs(int getR, int getC, int cnt) {

		visit[getR][getC]=true;
		
		if(getC == C-1) {	//종료 조건
			//show();
			state = 1;
			res++;
			return;
		}

		//3방탐색 하기
		for(int i=0; i<3; i++) {
			int tempR = getR+dr[i], tempC = getC+dc[i];
			if(inMap(tempR, tempC) && !visit[tempR][tempC] && map[tempR][tempC] == '.') {
				//System.out.println("check");
				visit[tempR][tempC] = true;
				map[tempR][tempC] = 'x';
				//show();
				dfs(tempR, tempC, cnt+1);
				if(state == 1)return;	//종료 조건이면 바로 나가기
				//visit[tempR][tempC] = false;
				//map[tempR][tempC] = '.';
			}

		}
	}

	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		// 결과를 한 번에 출력하기 위한 StringBuilder
		StringBuilder sb = new StringBuilder();

		String[] split = in.readLine().split(" ");
		//초기화, 입력
		R = Integer.parseInt(split[0]);
		C = Integer.parseInt(split[1]);
		res=0;
		visit = new boolean[R+1][C+1];
		map= new char[R+1][C+1]; 

		for(int i=0; i<R; i++) {
			String s = in.readLine();
			for(int j=0; j<C; j++) {
				map[i][j] = s.charAt(j);
			}
		}

		for(int i=0; i<R; i++) {
			state=0;
			dfs(i, 0, 0);
		}

		System.out.println(res);

	}

}