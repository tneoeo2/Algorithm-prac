import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int cnt = 0;
		int N = Integer.parseInt(br.readLine()); // 입력 받은 정수
		int res = N;
		while (true) {
			//(N % 10) * 10) : 새로운 10의자리 만들기
			N = ((N % 10) * 10) + (((N / 10) + (N % 10)) % 10);
			//System.out.println(N + " "); :확인용
			cnt++;

			if (res == N) {
				break;
			}
		}
		System.out.println(sb.append(cnt));
	}
}
