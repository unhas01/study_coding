import java.util.Scanner;

public class BJ_10807 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int N = input.nextInt();
		int arr [] = new int[N];
		for(int i = 0; i < N; i++)
			arr[i] = input.nextInt();
		
		int find = input.nextInt();
		int cnt = 0;
		for(int i = 0; i < N; i++) {
			if(arr[i] == find)
				cnt++;
		}
		
		System.out.println(cnt);
		
		input.close();
	}

}
