import java.util.Scanner;

public class Test {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] a = new int[N];
		for (int i = 0; i < N; i++) {
			System.out.println((i+1)+"번 째 정수입력 : ");
			a[i] = sc.nextInt();
		}
		Test t = new Test();
		
		System.out.println(t.sum(a));
		
	}
	public long sum (int[] a) {
		long ans = 0;
		for (int i = 0; i < a.length; i++) {
			ans += a[i];
		}
		return ans;
	}
	
}
