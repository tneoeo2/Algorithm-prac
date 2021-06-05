import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int sum = 0;
		String str = br.readLine();
		for (int i = 0; i < N; i++) {
			sum += str.charAt(i) - '0';	//charAt()는 해당 문자의 아스키 코드값을 반환
									// -48 또는 -'0'을 해줘야 입력받은 숫자값 사용가능
		}
		System.out.println(sum);

	}
}
