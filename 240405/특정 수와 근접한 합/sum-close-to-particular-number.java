import java.util.*;
import java.io.*;

public class Main {
    static int n,s;
    static ArrayList<Integer> numbers=new ArrayList<>();
    
    
    static int sumarr(ArrayList<Integer> arr){
        int sum=0;
        for(int i=0;i<arr.size();i++){
            sum=sum+arr.get(i);
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        n=Integer.parseInt(st.nextToken());
        s=Integer.parseInt(st.nextToken());

        st=new StringTokenizer(br.readLine());

        for(int i=0;i<n;i++){
            numbers.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(numbers);
        
        int min=0;
        int max=numbers.size()-1;
        int arrSum=sumarr(numbers);

        
        int diff = Math.abs(arrSum - s);
        int closestSum = arrSum;

        while(min<max){
            int currSum = arrSum - numbers.get(min) - numbers.get(max);
            int currDiff = Math.abs(currSum - s);

          if (currDiff < diff) {
                diff = currDiff;
                closestSum = currSum;
            }

            if (currSum > s) {
                min++;
            } else {
                max--;
            }
        }
        //System.out.println(closestSum);
        System.out.println(diff);
    }
}