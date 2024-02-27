import java.io.*;
import java.util.*;



public class Main {

	static int n,m;
	static TreeSet<Integer> ts=new TreeSet<>();

	public static void main(String[] args) throws IOException {

		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());

		n=Integer.parseInt(st.nextToken());

		for(int i=0;i<n;i++){
			st=new StringTokenizer(br.readLine());
			String cmd= st.nextToken();
			switch (cmd) {
				case "add":
					m = Integer.parseInt(st.nextToken());
					ts.add(m);
					break;
				case "largest":
					if(!ts.isEmpty()){
						System.out.println(ts.last());
						break;
					}else{
						System.out.println("None");
						break;
					}
				case "smallest":
					if(!ts.isEmpty()){
						System.out.println(ts.first());
						break;
					}else{
						System.out.println("None");
						break;
					}
				case "remove":
					m = Integer.parseInt(st.nextToken());
					if(!ts.isEmpty()&&ts.contains(m)){
						ts.remove(m);
						break;
					} else{
						System.out.println("None");
						break;
					}
				case "find":
					m = Integer.parseInt(st.nextToken());
					System.out.println(ts.contains(m));
					break;
				case "upper_bound":
					m = Integer.parseInt(st.nextToken());
					if(!ts.isEmpty()&&ts.higher(m)!=null){
						System.out.println(ts.higher(m));
						break;
					}
					else{
						System.out.println("None");
						break;
					}
				case "lower_bound":
					m = Integer.parseInt(st.nextToken());
					if(!ts.isEmpty()&&ts.ceiling(m)!=null){
						System.out.println(ts.ceiling(m));
						break;
					}
					else{
						System.out.println("None");
						break;
					}
			}

		}



	}
}