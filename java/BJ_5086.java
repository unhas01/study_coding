import java.io.*;
import java.util.StringTokenizer;

public class BJ_5086 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		String str;
		
		while(true) {
			str = br.readLine();
			if(str.equals("0 0"))
				break;
			
			StringTokenizer st = new StringTokenizer(str, " ");
			int n1 = Integer.parseInt(st.nextToken());
			int n2 = Integer.parseInt(st.nextToken());
			
			if(n2 % n1 == 0) {
				sb.append("factor\n");
			}
			else if(n1 % n2 == 0) {
				sb.append("multiple\n");
			}
			else {
				sb.append("neither\n");
			}
		}
		
		System.out.println(sb);
	}

}
