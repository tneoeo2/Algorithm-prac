import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	public static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) {
		boolean flg = true;
		int A = 0;
		int B = 0;
		List<Integer> resArr = new ArrayList<Integer>();
		while (flg) {
			A = sc.nextInt();
			B = sc.nextInt();
			if (A == 0 && B == 0) {
				flg = false;
			} else {
				resArr.add(A + B);

			}

		}
		for (int i = 0; i < resArr.size(); i++) {
			sb.append(resArr.get(i));
			sb.append("\n");
		}
		System.out.println(sb);
	}
}
