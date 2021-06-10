import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String S = br.readLine(); // 문자열 입력

		int[] arr = new int[26]; // 알파벳 배열

		for (int i = 0; i < arr.length; i++) {
			arr[i] = -1; // -1로 초기화
		}

		for (int i = 0; i < S.length(); i++) {
			char c = S.charAt(i);
			
			if (arr[c - 97] == -1) {
				arr[c - 97] = i; // 아스키코드 97 = a
			}
			
		}
		for (int j : arr) {

			System.out.print(j + " ");
		}
	}

}
