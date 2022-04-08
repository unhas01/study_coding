import java.io.*;
import java.util.StringTokenizer;

public class BJ_9093 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			
			while(st.hasMoreTokens()) {
				char c [] = st.nextToken().toCharArray();
				for(int j = c.length-1; j >= 0; j--) {
					sb.append(c[j]);
				}
				sb.append(" ");
			}
			
			sb.append("\n");
		}
		
		System.out.println(sb);
	}

}
