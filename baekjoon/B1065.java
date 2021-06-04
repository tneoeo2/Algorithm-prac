import java.util.Scanner;

public class Main {
//등차수열 : an =  a1 + (n-1)d	*d : 두항의 차이 n: n번 째항
//1~99 : 까지는 모두 등차수열이다
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); // N <=1000
		 int res = Main.getRes(N);
		
		System.out.println(res);

	}
	
	public static int getRes(int N) {
		
		
		int cnt = 0; // 한수의 개수
		
		if (N == 1000) {  //예외처리
			N = 999;
		}

		if (N < 100) {
			cnt = N;
		} else if (99 < N && N < 1000) {
			cnt = 99;
			
			while (N > 99) {
				
				int a3 = N / 100; // 백의자리
				int a2 = (N / 10)%10; // 십의자리
				int a1 = N % 10; // 일의자리
				//System.out.println(a3 + "/" + a2+ "/" + a1);

				if ((a3 - a2) == (a2 - a1)) { // 등차 수열이면
					cnt++; // 한수 개수 증가
				}
				
				N--;
			}
		}
		
		return cnt;
		
	}
}
