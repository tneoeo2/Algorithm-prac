import java.util.Scanner;
//nextLine() 엔터값 입력받을 때까지 기준으로 한줄 읽음
//next() 공백을 기준으로 하나의 문자열만 읽음

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();// 테스트케이스 개수 입력

		String[] arr = new String[T];
		int[] arr2 = new int[T];
		
		for (int j = 0; j < T; j++) {
			int R = Integer.parseInt(sc.next());
			String S = sc.next();
			
			arr[j] = S;
			arr2[j] = R;
		}
				
		for (int j = 0; j < arr.length; j++) { // 배열 반복
			for (int k = 0; k < arr[j].length(); k++) {	//문자의 길이 만큼 반복
				for (int k2 = 0; k2 < arr2[j]; k2++) {	//문자를 R번씩 반복하여 출력
					System.out.print(arr[j].charAt(k));
				}
			}
			System.out.println();
		}

	}

}
