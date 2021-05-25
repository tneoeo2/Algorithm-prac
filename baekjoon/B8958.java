import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		//테스트 케이스 갯수
		
		
		int N = Integer.parseInt(br.readLine());
		
		
		for(int i = 0; i < N; i++) {
			int score = 0; 
			int total = 0;
			String test = br.readLine();
			for (int j = 0; j < test.length(); j++) {
				if(test.charAt(j)=='O') {
					score++;
					total+=score;
				}else {
					score =0;
				}
			}
			System.out.println(total);
		}
		
		
	}


}
