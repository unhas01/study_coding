import java.io.*;

public class BJ_1259 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		String str;
		
		while(true) {
			str = br.readLine();
			if(str.equals("0"))
				break;
			
			StringBuffer buffer = new StringBuffer(str);
			String temp = buffer.reverse().toString();
			
			if(str.equals(temp))
				sb.append("yes\n");
			else
				sb.append("no\n");
		}
		
		System.out.println(sb);
	}

}
