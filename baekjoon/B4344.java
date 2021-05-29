import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// 테스트 케이스 갯수

		int N = Integer.parseInt(br.readLine());	
		
		StringTokenizer st;
		
		int[] arr;	//점수 배열
			//총합

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			
			int cnt = Integer.parseInt(st.nextToken()); //배열 인덱스 설정
			arr = new int[cnt];
			double sum = 0;
			
			for (int j = 0; j < cnt; j++) {
				arr[j] = Integer.parseInt(st.nextToken());
				sum += arr[j];	//총합 구하기
			}

			double mean = sum / cnt;	//평균
			double res = 0;	//평균이상 학생 수
			
			for (int k = 0; k < cnt; k++) {
				if (mean < arr[k]) {
					res++;
				}
			}
			System.out.printf("%.3f%%\n", (res / cnt)*100);
				
			}

	}

}
