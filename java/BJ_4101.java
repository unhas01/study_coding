import java.io.*;


public class BJ_4101 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		while(true) {
			String temp [] = br.readLine().split(" ");
			int n1 = Integer.parseInt(temp[0]);
			int n2 = Integer.parseInt(temp[1]);
			
			if(n1 == 0 && n2 == 0)
				break;
			
			if(n1 > n2)
				sb.append("Yes\n");
			else
				sb.append("No\n");
			
		}
		
		System.out.println(sb);
	}

}
