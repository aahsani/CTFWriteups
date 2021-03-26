

public class a2 {
    public String run(int i) {
        return xorHex("787d6c7f2c352b2c", "313333376d616e73313333376861");
    }

    public String xorHex(String str, String str2) {
        char[] cArr = new char[str.length()];
        int i = 0;
        for (int i2 = 0; i2 < cArr.length; i2++) {
            cArr[i2] = toHex(fromHex(str.charAt(i2)) ^ fromHex(str2.charAt(i2)));
        }
        StringBuilder sb = new StringBuilder();
        while (i < new String(cArr).length()) {
            int i3 = i + 2;
            sb.append((char) Integer.parseInt(new String(cArr).substring(i, i3), 16));
            i = i3;
        }
        return "{" + sb.toString().trim();
    }

    private int fromHex(char c) {
        if (c >= '0' && c <= '9') {
            return c - '0';
        }
        char c2 = 'A';
        if (c < 'A' || c > 'F') {
            c2 = 'a';
            if (c < 'a' || c > 'f') {
                throw new IllegalArgumentException();
            }
        }
        return (c - c2) + 10;
    }

    private char toHex(int i) {
        if (i >= 0 && i <= 15) {
            return "0123456789ABCDEF".charAt(i);
        }
        throw new IllegalArgumentException();
    }
}