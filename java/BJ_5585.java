import java.io.*;

public class BJ_5585 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int money = Integer.parseInt(br.readLine());
		int arr [] = {500, 100, 50, 10, 5, 1};
		money = 1000 - money;
		int cnt = 0;
		
		for(int i = 0; i < arr.length; i++) {
			int a = money / arr[i];
			int re = money % arr[i];
			money = re;
			cnt += a;
			
		}
		
		System.out.println(cnt);
	}

}
