import java.io.*;
import java.util.*;

public class Main {
	static int n;
	static int[] visited;
	static ArrayList<Integer> ans=new ArrayList<>();
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());

		visited=new int[n+1];
		choose(1);

	}
	static void choose(int cur){
		if(cur==n+1){
			for(int j=0;j<n;j++){
				System.out.print(ans.get(j)+" ");
			}
			System.out.print("\n");
			return;
		}
		for(int i=1;i<=n;i++){
			if(visited[i]==1) continue;

			visited[i]=1;
			ans.add(i);

			choose(cur+1);

			ans.remove(ans.size()-1);
			visited[i]=0;
		}

	}



}