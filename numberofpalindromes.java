package baek;

import java.util.Scanner;

public class numberofpalindromes {
	public static void main (String args[]) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();

		int result1 = 0;
		int result2 = 0;
		int result3 = 0;
		
		
		if(a < b && a < c) {
			result1 = a;
		}else if(b < a && b < c) {
			result1 = b;
		}else if(c < a && c < b) {
			result1 = c;
		}
		if((a > b && a < c)||(a < b && a > c)) {
			result2 = a;
		}else if((b > a && b < c)||b < a && b > c) {
			result2 = b;
		}else if((c > a && c < b)||(c < a && c > b)) {
			result2 = c;
		}
		if(a > b && a > c) {
			result3 = a;
		}else if(b > a && b > c) {
			result3 = b;
		}else if(c > a && c > b) {
			result3 = c;
		}
		
		System.out.print(result1 + " ");
		System.out.print(result2 + " ");
		System.out.print(result3);
	}
}
