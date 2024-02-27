import java.io.*;
import java.util.*;

public class Main {

	static int n,m;
	static HashMap<Integer,Integer> hm=new HashMap<>();

	public static void main(String[] args) throws IOException {

		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());

		n=Integer.parseInt(st.nextToken());
		m=Integer.parseInt(st.nextToken());

		st=new StringTokenizer(br.readLine());
		for(int i=0;i<n;i++){
			int num=Integer.parseInt(st.nextToken());
			if(!hm.containsKey(num)){
				hm.put(num,1);
			}else{
				hm.put(num,hm.get(num)+1);
			}
		}

		st=new StringTokenizer(br.readLine());
		for(int i=0;i<m;i++){
			int num=Integer.parseInt(st.nextToken());
			if(hm.containsKey(num)) {
				System.out.print(hm.get(num)+" ");
			}else{
				System.out.print(0+" ");
			}
		}





	}




}