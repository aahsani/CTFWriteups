
import java.security.MessageDigest;

public class a5 {
    /* JADX DEBUG: Failed to insert an additional move for type inference into block B:31:0x00ed */
    /* JADX DEBUG: Multi-variable search result rejected for r1v19, resolved type: java.lang.StringBuilder */
    /* JADX WARN: Multi-variable type inference failed */
    /* JADX WARN: Type inference failed for: r5v33 */
    /* JADX WARN: Type inference failed for: r5v35 */
    /* JADX WARN: Type inference failed for: r5v37 */
    /* JADX WARN: Type inference failed for: r5v39 */
    /* JADX WARN: Type inference failed for: r5v40, types: [java.lang.String] */
    /* JADX WARN: Type inference failed for: r5v43 */
    public String run(int i) {
        String[] strArr;
        String[] strArr2;
        String[] strArr3;
        String[] strArr4;
        String str;
        String[] strArr5;
        String[] strArr6 = {"!", "%", "="};
        String[] strArr7 = {"a", "b", "N"};
        String[] strArr8 = {"1", "G", "2"};
        String[] strArr9 = {"_", "%", "="};
        String[] strArr10 = {"A", "L", "D"};
        String str2 = "0";
        String[] strArr11 = {"R", str2, "$"};
        String[] strArr12 = {"C", "q", "3"};
        String[] strArr13 = {"4", "K", "("};
        String[] strArr14 = {"5", "J", "K"};
        int i2 = 0;
        while (true) {
            int i3 = 3;
            if (i2 >= 3) {
                return "y";
            }
            int i4 = 0;
            String[] strArr15 = strArr8;
            while (i4 < i3) {
                int i5 = 0;
                while (i5 < i3) {
                    int i6 = 0;
                    while (i6 < i3) {
                        String str3 = str2;
                        int i7 = 0;
                        while (i7 < i3) {
                            int i8 = 0;
                            while (i8 < i3) {
                                int i9 = 0;
                                while (i9 < i3) {
                                    int i10 = 0;
                                    while (i10 < i3) {
                                        int i11 = 0;
                                        while (i11 < i3) {
                                            String str4 = (strArr6[i2] + strArr7[i4] + strArr15[i5] + strArr9[i6] + strArr10[i7] + strArr11[i8] + strArr12[i9] + strArr13[i10] + strArr14[i11]) + "}";
                                            try {
                                                MessageDigest instance = MessageDigest.getInstance("MD5");
                                                strArr4 = strArr9;
                                                try {
                                                    instance.update(str4.getBytes());
                                                    byte[] digest = instance.digest();
                                                    StringBuilder sb = new StringBuilder();
                                                    strArr3 = strArr6;
                                                    try {
                                                        int length = digest.length;
                                                        strArr2 = strArr7;
                                                        int i12 = 0;
                                                        Object r5 = strArr15;
                                                        while (i12 < length) {
                                                            try {
                                                                String hexString = Integer.toHexString(digest[i12] & 255);
                                                                String[] strArr16 = (String[]) r5;
                                                                while (true) {
                                                                    strArr = strArr16;
                                                                    r5 = 2;
                                                                    if (hexString.length() >= 2) {
                                                                        break;
                                                                    }
                                                                    try {
                                                                        StringBuilder sb2 = new StringBuilder();
                                                                        r5 = str3;
                                                                        try {
                                                                            sb2.append((String) r5);
                                                                            sb2.append(hexString);
                                                                            hexString = sb2.toString();
                                                                            str3 = (String) r5;
                                                                            strArr16 = strArr;
                                                                        } catch (Exception e) {
                                                                            e = e;
                                                                            str = (String) r5;
                                                                            e.printStackTrace();
                                                                            i11++;
                                                                            str3 = str;
                                                                            strArr9 = strArr4;
                                                                            strArr6 = strArr3;
                                                                            strArr7 = strArr2;
                                                                            strArr15 = strArr;
                                                                            i3 = 3;
                                                                        }
                                                                    } catch (Exception e2) {
                                                                        //e = e2;
                                                                        str = str3;
                                                                        //e.printStackTrace();
                                                                        i11++;
                                                                        str3 = str;
                                                                        strArr9 = strArr4;
                                                                        strArr6 = strArr3;
                                                                        strArr7 = strArr2;
                                                                        strArr15 = strArr;
                                                                        i3 = 3;
                                                                    }
                                                                }
                                                                sb.append(hexString);
                                                                i12++;
                                                                str3 = str3;
                                                                length = length;
                                                                digest = digest;
                                                                r5 = strArr;
                                                            } catch (Exception e3) {
                                                                //e = e3;
                                                                strArr5 = (String[]) r5;
                                                                strArr = strArr5;
                                                                str = str3;
                                                                //e.printStackTrace();
                                                                i11++;
                                                                str3 = str;
                                                                strArr9 = strArr4;
                                                                strArr6 = strArr3;
                                                                strArr7 = strArr2;
                                                                strArr15 = strArr;
                                                                i3 = 3;
                                                            }
                                                        }
                                                        strArr = (String[]) r5;
                                                        str = str3;
                                                        if (sb.toString().equals("b469f80f05290ed415770ea56e69a476")) {
                                                            return str4;
                                                        }
                                                        i11++;
                                                        str3 = str;
                                                        strArr9 = strArr4;
                                                        strArr6 = strArr3;
                                                        strArr7 = strArr2;
                                                        strArr15 = strArr;
                                                        i3 = 3;
                                                    } catch (Exception e4) {
                                                        //e = e4;
                                                        strArr2 = strArr7;
                                                        strArr5 = strArr15;
                                                        strArr = strArr5;
                                                        str = str3;
                                                        //e.printStackTrace();
                                                        i11++;
                                                        str3 = str;
                                                        strArr9 = strArr4;
                                                        strArr6 = strArr3;
                                                        strArr7 = strArr2;
                                                        strArr15 = strArr;
                                                        i3 = 3;
                                                    }
                                                } catch (Exception e5) {
                                                    //e = e5;
                                                    strArr3 = strArr6;
                                                    strArr2 = strArr7;
                                                    strArr5 = strArr15;
                                                    strArr = strArr5;
                                                    str = str3;
                                                    //e.printStackTrace();
                                                    i11++;
                                                    str3 = str;
                                                    strArr9 = strArr4;
                                                    strArr6 = strArr3;
                                                    strArr7 = strArr2;
                                                    strArr15 = strArr;
                                                    i3 = 3;
                                                }
                                            } catch (Exception e6) {
                                                //e = e6;
                                                strArr4 = strArr9;
                                                strArr3 = strArr6;
                                                strArr2 = strArr7;
                                                strArr5 = strArr15;
                                                strArr = strArr5;
                                                str = str3;
                                                //e.printStackTrace();
                                                i11++;
                                                str3 = str;
                                                strArr9 = strArr4;
                                                strArr6 = strArr3;
                                                strArr7 = strArr2;
                                                strArr15 = strArr;
                                                i3 = 3;
                                            }
                                        }
                                        strArr = strArr15;
                                        i10++;
                                        strArr15 = strArr;
                                        i3 = 3;
                                    }
                                    strArr = strArr15;
                                    i9++;
                                    strArr12 = strArr12;
                                    strArr15 = strArr;
                                    i3 = 3;
                                }
                                strArr = strArr15;
                                i8++;
                                strArr13 = strArr13;
                                strArr15 = strArr;
                                i3 = 3;
                            }
                            strArr = strArr15;
                            i7++;
                            strArr14 = strArr14;
                            strArr15 = strArr;
                            i3 = 3;
                        }
                        strArr = strArr15;
                        i6++;
                        str2 = str3;
                        strArr15 = strArr;
                        i3 = 3;
                    }
                    strArr = strArr15;
                    i5++;
                    strArr15 = strArr;
                    i3 = 3;
                }
                strArr = strArr15;
                i4++;
                strArr15 = strArr;
                i3 = 3;
            }
            strArr = strArr15;
            i2++;
            strArr8 = strArr;
        }
    }
}