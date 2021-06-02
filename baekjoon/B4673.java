import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		
		List<Integer> nonSelf = new ArrayList<Integer>();
		
		
		for (int i = 0; i < 10001; i++) {
			int n = d(i);
			nonSelf.add(n);
		}
		
		int i = 0;
		
		while(i<10001) {	
			if(!nonSelf.contains(i)) {	//생성자가 있는 없는 수만 출력
			System.out.println(i);
			}
			i++;
		}

		
	}
	
	public static int d (int number) {
			
		int sum = number;
		while(number != 0) {	//number 가 0이 될때까지 반복
			sum = sum + (number%10);	//number%10 첫째자리수
			number = number/10; //첫째자리수 제거
		}
		
		return sum;	//생성자가 있는 수
			
	}

}
