import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int cnt = N;
		int i = 0;
		int[] arr = new int[N];
		
		while (cnt != 0) {
			arr[i++] = Integer.parseInt(st.nextToken());
			cnt--;
		}
		Arrays.sort(arr);
		System.out.println(sb.append(arr[0]).append(" ").append(arr[N - 1]));
	}
}
