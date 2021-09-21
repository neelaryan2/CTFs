import java.util.Scanner;

public class multipleDimensions {
	
	private char[][] arr;
	private String mrByrds;
	
	public multipleDimensions() {
		mrByrds = "hey_since_when_was_time_>B?\\mension?";
		arr = new char[6][6];
		for (int i = 0; i < mrByrds.length(); i++) {
			arr[i / 6][i % 6] = mrByrds.charAt(i);
		}
	}

	public void line() {
		char[][] newArr = new char[arr.length][arr[0].length];
		for (int i = 5; i >= 0; i--) {
			for (int j = 5; j >= 0; j--) {
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
				newArr[i][j] = (char) (arr[p][q] - f);
			}
		}
		arr = newArr;
	}

	public String check() {
		String genStr = "";
		int n = 6;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				genStr += arr[j][i];
			}
		}
		return genStr;
	}
	
	public void plane() {
		int n = arr.length;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				arr[i][j] -= i + n - j;
			}
		}

		for (int i = 2; i >= 0; i--) {
			for (int j = 2; j >= 0; j--) {
				char t = arr[i][j];
				arr[i][j] = arr[n - 1 - j][i];
				arr[n - 1 - j][i] = arr[n - 1 - i][n - 1 - j];
				arr[n - 1 - i][n - 1 - j] = arr[j][n - 1 -i];
				arr[j][n - 1 -i] = t;
			}
		}
		
	}
	
	public void space(int n) {
		arr[(35 - n) / 6][(35 - n) % 6] += (n / 6) + (n % 6);
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
				arr[i][j] -= t[j][i];
	}
	
	public static void main(String[] args) {
		multipleDimensions testingTravel = new multipleDimensions();
		testingTravel.time();
		testingTravel.space(35);
		testingTravel.plane();
		testingTravel.line();
		System.out.println(testingTravel.check());
	}
}
