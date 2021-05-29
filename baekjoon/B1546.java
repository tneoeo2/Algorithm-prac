import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine()); //시험본 과목 개수
		
		double[] arr = new double[N];
		
		double sum = 0.0;
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");;
		double M = -1;
			
			for (int i = 0; i < N; i++) {
			arr[i] = Double.parseDouble(st.nextToken());	//점수를 배열에 넣어줌
			sum += arr[i];
		}
			Arrays.sort(arr);
			M = arr[N-1];
		System.out.println((sum/M)*100.0/N);
	}

}
