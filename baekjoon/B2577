
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
		public static void main (String[] args){
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			
			try {
				int A = Integer.parseInt(br.readLine());
				int B = Integer.parseInt(br.readLine());
				int C = Integer.parseInt(br.readLine());
				
				 
				 int[] counts = new int[10];
				 String res = String.valueOf(A*B*C); //값을 String로 전환
				 for(int i = 0; i <res.length(); i++) {
					 counts[res.charAt(i)-'0']++;		// charAt(i) - '0' char->int형변환	
				 }
				 //System.out.println(res);
				 for (int j = 0; j < counts.length; j++) {
					System.out.println(counts[j]);
				}
				 
			}catch (Exception e) {
				// TODO: handle exception
			}
		}
			
		
}
