import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main
{
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int [][]arr = new int[20][20];
		
		for(int i=1; i<=19; i++){
		    String[] temp = br.readLine().split(" ");
		    for(int j=1; j<=19; j++){
		        arr[i][j] = Integer.parseInt(temp[j-1]);
		    }
		}
		/*
		for(int i=1; i<=19; i++){
		    for(int j=1; j<=19; j++){
		        System.out.print(arr[i][j]+" ");
		    }System.out.println();
		}
		*/
		
		// solve - 8방향 탐색
		int dr[] = {-1, 0, 1, 1, 1, 0, -1, -1};
		int dc[] = {1, 1, 1, 0, -1, -1, -1, 0};
		for(int i=1; i<=19; i++){
		    for(int j=1; j<=19; j++){
		   //int i=3,j=2;
		        if(arr[i][j] != 0){ 
		            //1, 2이면 8방 탐색 직진
		           // System.out.println(i+" 탐색 "+j);
		           
		            for(int ii=0; ii<4; ii++){
		                //System.out.println("8탐색");
		                
		                int cnt=1;  //정답 도출을 위한 cnt
		                int temp=arr[i][j];
		                int[][] getRes = {{i,j}, {0,0}};
		                
		                int r=i+dr[ii], c=j+dc[ii]; 
		                while(0<r && r<20 && 0<c && c<20 && temp == arr[r][c]){
		                    //System.out.print("1while ");
		                    //System.out.println(r+" "+c + " "+ cnt);
		                    cnt++;
                            if(cnt == 5){
		                        getRes[1][0]=r; getRes[1][1]=c;
		                    }
		                    r+=dr[ii]; c+=dc[ii];
		                }
		                r=i+dr[ii+4]; c=j+dc[ii+4]; 
		                while(0<r && r<20 && 0<c && c<20 && temp == arr[r][c]){
		                    //System.out.print("2while ");
		                    //System.out.println(r+" "+c +  " " +cnt);
		                    cnt++;
		                    if(cnt == 5){
		                        getRes[1][0]=r; getRes[1][1]=c;
		                    }
		                    r+=dr[ii+4]; c+=dc[ii+4];
		                }
		                
		                if(cnt == 5){
		                    int resR,resC;
		                    if(getRes[0][1] > getRes[1][1]){
		                        resR=getRes[1][0];  resC=getRes[1][1];
		                    } else if(getRes[0][1] < getRes[1][1]){
		                         resR=getRes[0][0];  resC=getRes[0][1];
		                    } else {
		                        if(getRes[0][0] > getRes[1][0]){
		                             resR=getRes[1][0];  resC=getRes[1][1];
		                        } else {
		                             resR=getRes[0][0];  resC=getRes[0][1];
		                        }  
		                    }
		                    System.out.println(arr[resR][resC]);
		                    System.out.print(resR+" "+resC);
		                    return;
		                }
		                
		            }
		        }
		    }
		}
		System.out.println("0");
		
		
		
		
		
	}
}

