import java.io.*;
import java.util.*;

public class Main {

	static int n;
	static HashMap<Integer,Integer> hm=new HashMap<>();

	public static void main(String[] args) throws IOException {

		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());

		n=Integer.parseInt(st.nextToken());

		for(int i=0;i<n;i++){
			st=new StringTokenizer(br.readLine());
			String cmd=st.nextToken();


			if(cmd.equals("add")){
				int k=Integer.parseInt(st.nextToken());
				int v=Integer.parseInt(st.nextToken());
				hm.put(k,v);
			}else if(cmd.equals("find")){
				int k=Integer.parseInt(st.nextToken());
				if (hm.containsKey(k)) {
					System.out.println(hm.get(k));
				}else{
					System.out.println("None");
				}
			}else{
				int k=Integer.parseInt(st.nextToken());
				hm.remove(k);
			}


		}


	}




}