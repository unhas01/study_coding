import java.io.IOException;
import java.util.Scanner;

public class BJ_1541 {

	public static void main(String[] args) throws IOException{
		
		Scanner sc= new Scanner(System.in);
        String input = sc.nextLine();
        String [] arr = input.split("\\-");
        
        int result = add(arr[0]);
        for(int i = 1;i < arr.length; i++) {
            result -= add(arr[i]);
        }
        System.out.println(result);

        sc.close();
	}
	public static int add(String i) {
        String arr [] = i.split("\\+");
        int result = 0;
        for(String k : arr) {
            result+=Integer.parseInt(k);
        }
        

        return result;
    }
}
