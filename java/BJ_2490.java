import java.io.*;

public class BJ_2490 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		for(int i = 0; i < 3; i++) {
			String s[] = br.readLine().split(" ");
			int cnt = 0;
			for(int j = 0; j < s.length; j++) {
				if(s[j].equals("0")) {
					cnt++;
				}
			}
			if(cnt == 1) {
				sb.append("A\n");
			}
			else if(cnt == 2) {
				sb.append("B\n");
			}
			else if(cnt == 3) {
				sb.append("C\n");
			}
			else if(cnt == 4) {
				sb.append("D\n");
			}
			else {
				sb.append("E\n");
			}
		}
		System.out.println(sb);
		
	}

}
