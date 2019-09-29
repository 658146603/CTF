package test;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class CTF_JAVA {
    private static byte[] b = {23, 22, 26, 26, 25, 25, 25, 26, 27, 28, 30, 30, 29, 30, 32, 32};

    public static String checkSN(String paramString1) {
        if (paramString1 != null) {
            try {
                Object localObject = MessageDigest.getInstance("MD5");
                ((MessageDigest) localObject).reset();
                ((MessageDigest) localObject).update(paramString1.getBytes());
                paramString1 = toHexString(((MessageDigest) localObject).digest(), "");
                localObject = new StringBuilder();
                int i = 0;
                while (i < paramString1.length()) {
                    ((StringBuilder) localObject).append(paramString1.charAt(i));
                    i += 2;
                }
                paramString1 = ((StringBuilder) localObject).toString();
                return ("flag{" + paramString1 + "}");
            } catch (NoSuchAlgorithmException e) {
                e.printStackTrace();
            }
        }

        return "";
    }

    private static String toHexString(byte[] paramArrayOfByte, String paramString) {
        StringBuilder localStringBuilder = new StringBuilder();
        int j = paramArrayOfByte.length;
        int i = 0;
        while (i < j) {
            String str = Integer.toHexString(paramArrayOfByte[i] & 0xFF);
            if (str.length() == 1)
                localStringBuilder.append('0');
            localStringBuilder.append(str).append(paramString);
            i += 1;
        }
        return localStringBuilder.toString();
    }

    public static String getFlag() {
        byte[] arrayOfByte2 = new byte[16];
        for (int i = 0; i < 16; i++) {
            arrayOfByte2[i] = (byte) (i + 122 - 2 * b[i]);
        }

        return new String(arrayOfByte2);
    }

    public static String check(String paramString) {
        byte[] arrayOfByte1 = paramString.getBytes();
        byte[] arrayOfByte2 = new byte[16];
        int i = 0;
        while (i < 16) {
            arrayOfByte2[i] = ((byte) ((arrayOfByte1[i] + b[i]) % 61));
            i += 1;
        }
        i = 0;
        while (i < 16) {
            arrayOfByte2[i] = ((byte) (arrayOfByte2[i] * 2 - i));
            i += 1;
        }
        return new String(arrayOfByte2);
    }

    public static void re() {

    }

    private static final byte[] p = {
            -40, -62, 107, 66, -126, 103, -56, 77, 122, -107,
            -24, -127, 72, -63, -98, 64, -24, -5, -49, -26,
            79, -70, -26, -81, 120, 25, 111, -100, -23, -9,
            122, -35, 66, -50, -116, 3, -72, 102, -45, -85,
            0, 126, -34, 62, 83, -34, 48, -111, 61, -9,
            -51, 114, 20, 81, -126, -18, 27, -115, -76, -116,
            -48, -118, -10, -102, -106, 113, -104, 98, -109, 74,
            48, 47, -100, -88, 121, 22, -63, -32, -20, -41,
            -27, -20, -118, 100, -76, 70, -49, -39, -27, -106,
            -13, -108, 115, -87, -1, -22, -53, 21, -100, 124,
            -95, -40, 62, -69, 29, 56, -53, 85, -48, 25,
            37, -78, 11, -110, -24, -120, -82, 6, -94, -101 };

    private static final byte[] q = {
            -57, -90, 53, -71, -117, 98, 62, 98, 101, -96,
            36, 110, 77, -83, -121, 2, -48, 94, -106, -56,
            -49, -80, -1, 83, 75, 66, -44, 74, 2, -36,
            -42, -103, 6, -115, -40, 69, -107, 85, -78, -49,
            54, 78, -26, 15, 98, -70, 8, -90, 94, -61,
            -84, 64, 112, 51, -29, -34, 126, -21, -126, -71,
            -31, -24, -60, -2, -81, 66, -84, 85, -91, 10,
            84, 70, -8, -63, 26, 126, -76, -104, -123, -71,
            -126, -62, -23, 11, -39, 70, 14, 59, -101, -39,
            -124, 91, -109, 102, -49, 21, 105, 0, 37, Byte.MIN_VALUE,
            -57, 117, 110, -115, -86, 56, 25, -46, -55, 7,
            -125, 109, 76, 104, -15, 82, -53, 18, -28, -24 };

    static String i() {
        byte b2 = 0;
        byte[] arrayOfByte1 = new byte[p.length];
        byte b1;
        for (b1 = 0; b1 < arrayOfByte1.length; b1++)
            arrayOfByte1[b1] = (byte)(p[b1] ^ q[b1]);
        byte b = arrayOfByte1[0];
        for (b1 = 0; arrayOfByte1[b + b1] != 0; b1++);
        byte[] arrayOfByte2 = new byte[b1];
        while (b2 < b1) {
            arrayOfByte2[b2] = arrayOfByte1[b + b2];
            b2++;
        }
        return new String(arrayOfByte2);
    }


}
