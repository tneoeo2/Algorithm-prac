import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		
		int[] arr = new int[9]; //배열 초기화
		int i = 0;
		int cnt = 0;
		while (cnt != 9) {
			arr[i++] = Integer.parseInt(br.readLine());
			cnt++;
		}
		
		int maxCnt = 0;	//최댓값
		int maxIndex = 0;							//최댓값의 인덱스
		
		for (int res : arr) {
			if (res > maxCnt) {
				maxCnt=res;
			}
		}
		
		for (int j = 0; j < arr.length; j++) {
			if(arr[j] == maxCnt) {
				maxIndex = j+1;
			};
			
		}
		
		
		System.out.println(sb.append(maxCnt).append("\n").append(maxIndex));
		
	}

	

}
