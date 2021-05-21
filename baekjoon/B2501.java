import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//백준 
public class Main {
	public static void main(String[] args) throws IndexOutOfBoundsException {
		Scanner sc = new Scanner(System.in);
		
		//N과 K
		// N >=1 N<= 10000
		// K >=1 K <=N
		 
		 int N = sc.nextInt(); 
		 int K = sc.nextInt();
		 List<Integer> arrList = new ArrayList<>();
		 for(int i = 1; i<=N; i++) {
			 if((N%i)==0) {
				 arrList.add(i);
			 }
		 }
		 try {
		 System.out.println(arrList.get(K-1));
		 }catch (IndexOutOfBoundsException e) {
			 System.out.println(0);
		}
	}
}