import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import java.util.Base64;
import java.util.Arrays;
import javax.crypto.Cipher;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;

class AllPermutation {
	private final char Arr[];
	private int Indexes[];
	private int Increase;

	public AllPermutation(char arr[]) {
		this.Arr = arr;
		this.Increase = -1;
		this.Indexes = new int[this.Arr.length];
	}

	public void GetFirst() {
		this.Indexes = new int[this.Arr.length];
		for (int i = 0; i < Indexes.length; ++i) {
			this.Indexes[i] = i;
		}
		this.Increase = 0;
	}

	public boolean HasNext() {
		return this.Increase != (this.Indexes.length - 1);
	}

	public void GetNext() {
		if (this.Increase == 0) {
			this.Swap(this.Increase, this.Increase + 1);
			this.Increase += 1;
			while (this.Increase < this.Indexes.length - 1
					&& this.Indexes[this.Increase]
					> this.Indexes[this.Increase + 1]) {
				++this.Increase;
			}
		} else {
			if (this.Indexes[this.Increase + 1] > this.Indexes[0]) {
				this.Swap(this.Increase + 1, 0);
			} else {
				int start = 0;
				int end = this.Increase;
				int mid = (start + end) / 2;
				int tVal = this.Indexes[this.Increase + 1];
				while (!(this.Indexes[mid] < tVal && this.Indexes[mid - 1] > tVal)) {
					if (this.Indexes[mid] < tVal) {
						end = mid - 1;
					} else {
						start = mid + 1;
					}
					mid = (start + end) / 2;
				}
				this.Swap(this.Increase + 1, mid);
			}
			for (int i = 0; i <= this.Increase / 2; ++i) {
				this.Swap(i, this.Increase - i);
			}
			this.Increase = 0;
		}
	}

	public char[] Output() {
		char[] out = new char[this.Arr.length];
		for (int i = 0; i < this.Indexes.length; ++i) {
			out[i] = this.Arr[this.Indexes[i]];
		}
		return out;
	}

	private void Swap(int p, int q) {
		int tmp = this.Indexes[p];
		this.Indexes[p] = this.Indexes[q];
		this.Indexes[q] = tmp;
	}
}

public class Main {
	public static char[] p_array = new char[] {'g', 'o', '0', 'd', '$', 'l', 'u', 'c', 'k'};
	public static byte[] CHECK_SALT = new byte[] { -34, -83, -66, -17};
	public static byte[] DECRYPT_SALT = new byte[] {17, 34, 51, 68};
	public static String encryption_iv = "pJoKGZlx+tbr38ooZGNYeg==";
	public static String encrypted_flag = "ajVD6Q7SS9ma7ghrOEG1Z1Tn0+RBlK/Rhntt4QVI8Iq0K6HZxkEfvVpnFk9utep2";

	public static int check() {
		StringBuilder sb = new StringBuilder();
		for (int k = 0; k < p_array.length; ++k) {
			sb.append(p_array[k]);
			if (k < 3) continue;
			String s = sb.toString();
			if (toHex(pbkdf2(s, CHECK_SALT)).equals("8045a9b6d9eece98352e353c9091f353")) {
				byte[] key = pbkdf2(s, DECRYPT_SALT);
				String flag = decrypt_flag(key);
				System.out.println(flag);
				return 1;
			}
		}
		return 0;
	}
	private static String toHex(byte[] data) {
		StringBuilder s = new StringBuilder();
		for (int i = 0; i < data.length; ++i) {
			s.append(String.format("%02x", data[i]));
		}
		return s.toString();
	}

	public static byte[] pbkdf2(String password, byte[] salt) {
		try {
			PBEKeySpec spec = new PBEKeySpec(password.toCharArray(), salt, 1500, 128);
			SecretKeyFactory skf = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");
			return skf.generateSecret(spec).getEncoded();
		} catch (NoSuchAlgorithmException var4) {
			System.out.println("[-] No such algorithm");
			return null;
		} catch (InvalidKeySpecException var5) {
			System.out.println("[-] No such keyspec");
			return null;
		}
	}

	public static String decrypt_flag(byte[] key) {
		try {
			SecretKeySpec secretKey = new SecretKeySpec(key, "AES");
			Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
			IvParameterSpec ivspec = new IvParameterSpec(Base64.getDecoder().decode(encryption_iv));
			cipher.init(2, secretKey, ivspec);
			return new String(cipher.doFinal(Base64.getDecoder().decode(encrypted_flag)));
		} catch (Exception var4) {
			return var4.toString();
		}
	}

	public static void main(String[] args) {
		AllPermutation perm = new AllPermutation(p_array);
		perm.GetFirst();
		int i, found;
		found = check();
		if (found != 0) {
			return;
		}
		int counter = 1;
		int already_done = 338132;
		while (already_done != 0) {
			already_done--;
			counter++;
			perm.GetNext();
		}
		p_array = perm.Output();
		while (perm.HasNext()) {
			found = check();
			if (found != 0) {
				return;
			}
			counter++;
			System.out.println(counter);
			perm.GetNext();
			p_array = perm.Output();
		}
	}
}
