import java.io.*;
import java.util.*;



public class Main {

	static int n,m;
	static class Person implements Comparable<Person>{
		String name;
		int height,weight;
		public Person(String name,int height,int weight){
			this.name=name;
			this.height=height;
			this.weight=weight;
		}
		@Override
		public int compareTo(Person person){
			return this.height-person.height;
		}
	}


	public static void main(String[] args) throws IOException {

		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		n=Integer.parseInt(st.nextToken());

		Person[] persons=new Person[n];

		for(int i=0;i<n;i++){
			st=new StringTokenizer(br.readLine());
			String name=st.nextToken();
			int height=Integer.parseInt(st.nextToken());
			int weight=Integer.parseInt(st.nextToken());

			persons[i]=new Person(name,height,weight);
		}

		Arrays.sort(persons);

		for(int i=0;i<n;i++){
			System.out.println(persons[i].name+" "+persons[i].height+" "+persons[i].weight);
		}



	}
}