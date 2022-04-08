import java.io.*;

public class BJ_1032 {

	public static void main(String[] args) throws IOException{
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String s [] = new String[N];
		
		for(int i = 0; i < N; i++) {
			s[i] = br.readLine();
		}
		StringBuilder sb = new StringBuilder();
		boolean chk = true;
		for(int i = 0; i < s[0].length(); i++) {
			char c = s[0].charAt(i);
			chk = true;
			for(int j = 1; j < N; j++) {
				if(c != s[j].charAt(i)) {
					chk = false;
					break;
				}
			}
			
			if(chk == true) {
				sb.append(c);
			} else
				sb.append('?');
		}
		System.out.println(sb);
	}

}
