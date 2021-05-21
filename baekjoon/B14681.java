import java.util.Scanner;

//백준 제출용
public class Main {
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		int x = sc.nextInt();
		
		int y = sc.nextInt();
		
		
		if(x > 0 && y >0) {
			System.out.println(1);
		}else if(x>0 && y<0) {
			System.out.println(4);
		}else if(x<0 && y>0) {
			System.out.println(2);
		}else {
			System.out.println(3);
		}
	}
}
