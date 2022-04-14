import java.io.*;

public class BJ_2010 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new  BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int sum = 0;
		
		for(int i = 0; i < N; i++) {
			int num = Integer.parseInt(br.readLine());
			sum += num;
		}
		
		System.out.println(sum - (N - 1));
	}

}
