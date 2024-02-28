import java.io.*;
import java.util.*;

public class Main {
	static int n;
	static int[][] arr;
	static int[] visited;
	static ArrayList<Integer> ans=new ArrayList<>();
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());

		visited=new int[n+1];
		arr=new int[n+1][n+1];
		for(int i=1;i<=n;i++){
			st = new StringTokenizer(br.readLine());
			for(int j=1;j<=n;j++){
				arr[i][j]=Integer.parseInt(st.nextToken());
			}
		}
		choose(1,0);
		System.out.println(max);

	}
	static int max=0;

	static void choose(int cur,int sum){

		if(cur==n+1){
			max=Math.max(max,sum);
			return;
		}
		for(int i=1;i<=n;i++){
			if(visited[i]==1) continue;
			visited[i]=1;
			choose(cur+1,sum+arr[cur][i]);
			visited[i]=0;
		}


	}



}