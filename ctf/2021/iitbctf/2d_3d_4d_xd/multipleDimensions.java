import java.util.Scanner;

public class multipleDimensions {
	
	private char[][] arr;
	private String mrByrds;
	
	public multipleDimensions(String s) {
		arr = new char[6][6];
		for (int i = 0; i < s.length(); i++) {
			arr[i % 6][i / 6] = s.charAt(i);
		}
		mrByrds = "hey_since_when_was_time_>B?\\mension?";
	}

	public void line() {
		char[][] newArr = new char[arr.length][arr[0].length];
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[0].length; j++) {
				int p = i - 1, q = j - 1, f = 0;
				boolean row = i % 2 == 0;
				boolean col = j % 2 == 0;
				if (row) {
					p = i + 1;
					f++;
				} else
					f--;
				if (col) {
					q = j + 1;
					f++;
				} else
					f--;
				newArr[p][q] = (char) (arr[i][j] + f);
			}
		}
		arr = newArr;
	}

	public boolean check() {
		String genStr = "";
		for (char[] row: arr)
			for (char c: row)
				{genStr += c;}	
		return genStr.equals(mrByrds);
	}
	
	public void plane() {
		int n = arr.length;
		for (int i = 0; i < n / 2; i++) {
			for (int j = 0; j < n / 2; j++) {
				char t = arr[j][n - 1 -i];
				arr[j][n - 1 -i] = arr[n - 1 - i][n - 1 - j];
				arr[n - 1 - i][n - 1 - j] = arr[n - 1 - j][i];
				arr[n - 1 - j][i] = arr[i][j];
				arr[i][j] = t;
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				arr[i][j] += i + n - j;
			}
		}
	}
	
	public void space(int n) {
		arr[(35 - n) / 6][(35 - n) % 6] -= (n / 6) + (n % 6);
		if (n != 0) {
			n--;
			space(n);
		}
	}
	
	public void time() {
		int[][] t = {
				{8, 65, -18, -21, -15, 55}, 
				{8, 48, 57, 63, -13, 5}, 
				{16, -5, -26, 54, -7, -2}, 
				{48, 49, 65, 57, 2, 10}, 
				{9, -2, -1, -9, -11, -10}, 
				{56, 53, 18, 42, -28, 5}
			};
		for (int j = 0; j < arr[0].length; j++)
			for (int i = 0; i < arr.length; i++)
				arr[i][j] += t[j][i];
	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Enter Your flag: ");
		String s = in.next();
		if (s.length() == 36) {
			multipleDimensions testingTravel = new multipleDimensions(s);
			testingTravel.line();
			testingTravel.plane();
			testingTravel.space(35);
			testingTravel.time();
			if (testingTravel.check())
				System.out.println("Congratulations! You have transcended beyond all the dimensions 😲");
			else
				System.out.println("Oops, that's incorrect");
		} 
		else {
			System.out.println("Oops, that's incorrect.");
		}
		in.close();
	}
}
