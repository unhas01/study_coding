import java.io.*;

public class BJ_1748 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int count = 1;
		int temp = 0;
        int lenght = 10;
        for(int i = 1; i <= N; i++) {
            if(i == lenght) {
                count++;
                lenght = lenght * 10;
            }
            temp = temp + count;
        }
        System.out.println(temp);
		
	}

}
