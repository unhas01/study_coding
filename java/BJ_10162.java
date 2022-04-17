import java.io.*;

public class BJ_10162 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		int time [] = {300, 60, 10};
		int cnt1 = 0;
		int cnt2 = 0;
		int cnt3 = 0;
		
//		while(true) {
//			int a = T / time[0];
//			int re = T % time[0];
//			T = re;
//			cnt1 += a;
//		}
		for(int i = 0; i < time.length; i++) {
			int a = T / time[i];
			int re = T % time[i];
			T = re;
			if(i == 0) {
				cnt1 += a;
			}
			if(i == 1) {
				cnt2 += a;
			}
			if(i == 2) {
				cnt3 += a;
			}
		}
		if(T == 0) {
			System.out.println(cnt1 + " " + cnt2 + " " + cnt3);
		}else {
			System.out.println("-1");
		}
		
		
	}

}
