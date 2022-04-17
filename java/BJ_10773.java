import java.io.*;
import java.util.*;

public class BJ_10773 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Stack<Integer> stack = new Stack<Integer>();
		
		int K = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < K; i++) {
			int n = Integer.parseInt(br.readLine());
			
			if(n == 0) {
				stack.pop();
			}
			else {
				stack.push(n);
			}
		}
		
		int sum = 0;
		
		for(int i : stack) {
			sum += i;
		}
		
		System.out.println(sum);
	}

}
