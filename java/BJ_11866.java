import java.io.*;
import java.util.*;

public class BJ_11866 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		String s [] = br.readLine().split(" ");
		int N = Integer.parseInt(s[0]);
		int K = Integer.parseInt(s[1]);
		
		LinkedList<Integer> ls = new LinkedList<>();
		sb.append("<");
		
		for(int i = 1; i <= N; i++) {
			ls.add(i);
		}
		
		int index = 0;
		
		while(N > 1) {
			index = (index + (K - 1)) % N;
		
			sb.append(ls.remove(index)).append(", "); 
			N--;
		}
		
		sb.append(ls.remove()).append(">");
		System.out.println(sb);
	}

}
