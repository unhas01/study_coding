import java.io.*;

public class BJ_10886 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int arr[] = new int[N];
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
	
		int cnt1 = 0;
		int cnt2 = 0;
		
		for(int i = 0; i < N; i++) {
			if(arr[i] == 0) {
				cnt1++;
			}
			else {
				cnt2++;
			}
		}
		
		if(cnt1 > cnt2) {
			System.out.println("Junhee is not cute!");
		}
		else {
			System.out.println("Junhee is cute!");
		}
	}

}
