import java.io.*;

public class BJ_2810 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String str = br.readLine();
		int cnt = 1;
		
		for(int i = 0; i < N; i++) {
			char c = str.charAt(i);	
			if(c == 'S')
				cnt++;
			else if(c == 'L') {
				i++;
				cnt++;
			}
					
		}
		
		if(cnt > N) System.out.println(N);
		else System.out.println(cnt);
	}

}
