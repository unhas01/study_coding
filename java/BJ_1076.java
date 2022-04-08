import java.io.*;

public class BJ_1076 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String color [] = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
		int value [] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
		long multi [] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};
		
		String c1 = br.readLine();
		String c2 = br.readLine();
		String c3 = br.readLine();
		
		int index = 0;
		
		for(int i = 0; i < color.length; i++) {
			if(c1.equals(color[i]))
				index = i;
		}
		
		String res = "";
		res += value[index];
		
		for(int i = 0; i < color.length; i++) {
			if(c2.equals(color[i]))
				index = i;
		}
		res += value[index];
		
//		System.out.println(res);
		
		for(int i = 0; i < color.length; i++) {
			if(c3.equals(color[i]))
				index = i;
		}
		long result = 0;
		result = Integer.parseInt(res);
		result *= multi[index];
		
		System.out.println(result);
		
		
	}

}
