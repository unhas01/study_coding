import java.io.*;

public class BJ_2902 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		String s [] = br.readLine().split("-");
		
		for(int i = 0; i < s.length; i++) {
			char c = s[i].charAt(0);
			sb.append(c);
		}
		
		System.out.println(sb);
	}

}
