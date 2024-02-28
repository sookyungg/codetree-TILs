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

		choose(1);
		System.out.println(min);

	}
	static int min=Integer.MAX_VALUE;

	static void choose(int cur){

		if(cur==n){

			//System.out.println(ans);
			int sum=0;

			for(int i=0;i<n-2;i++){
				if(i==0) sum+=arr[1][ans.get(i)];
				if(i==n-3) sum+=arr[ans.get(i)][1];
				sum+=arr[ans.get(i)][ans.get(i+1)];
			}

			min=Math.min(min,sum);

			return;
		}

		for(int i=2;i<=n;i++){
			if(visited[i]==1) continue;

			visited[i]=1;

			ans.add(i);
			choose(cur+1);

			ans.remove(ans.size()-1);
			visited[i]=0;
		}


	}



}