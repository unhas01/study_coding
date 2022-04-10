import java.io.*;

public class BJ_20154 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String alpa [] = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
				"S", "T", "U", "V", "W", "X", "Y", "Z"};
		int arr [] = {3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1};
		
		String s [] = br.readLine().split("");
		int temp [] = new int[s.length];
		
		for(int i = 0; i < temp.length; i++) {
			int index = 0;
			for(int j = 0; j < alpa.length; j++) {
				if(s[i].equals(alpa[j]))
					index = j;
			}
			
			temp[i] = arr[index];
		}
		int sum = 0;
		for(int i = 0; i < temp.length; i++) {
			sum += temp[i];
		}
		
		if(sum % 2 == 0) {
			System.out.println("You're the winner?");
		}
		else {
			System.out.println("I'm a winner!");
		}
	}

}
