package ctf;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class CTF1 {
//    public static String checkSN(String paramString1)
//    {
//        if (paramString1 != null) {
//            try
//            {
//                Object localObject = MessageDigest.getInstance("MD5");
//                ((MessageDigest)localObject).reset();
//                ((MessageDigest)localObject).update(paramString1.getBytes());
//                paramString1 = toHexString(((MessageDigest)localObject).digest(), "");
//                localObject = new StringBuilder();
//                int i = 0;
//                while (i < paramString1.length())
//                {
//                    ((StringBuilder)localObject).append(paramString1.charAt(i));
//                    i += 2;
//                }
//                paramString1 = ((StringBuilder)localObject).toString();
//                return  ("flag{" + paramString1 + "}");
//            }
//            catch (NoSuchAlgorithmException e)
//            {
//                e.printStackTrace();
//            }
//        }
//
//        return "";
//    }
//
//    private static String toHexString(byte[] paramArrayOfByte, String paramString)
//    {
//        StringBuilder localStringBuilder = new StringBuilder();
//        int j = paramArrayOfByte.length;
//        int i = 0;
//        while (i < j)
//        {
//            String str = Integer.toHexString(paramArrayOfByte[i] & 0xFF);
//            if (str.length() == 1)
//                localStringBuilder.append('0');
//            localStringBuilder.append(str).append(paramString);
//            i += 1;
//        }
//        return localStringBuilder.toString();
//    }
//
//
//    private static byte[] b = { 23, 22, 26, 26, 25, 25, 25, 26, 27, 28, 30, 30, 29, 30, 32, 32 };
//
//    public static String getFlag() {
//        byte[] arrayOfByte2 = new byte[16];
//        for (int i=0; i< 16; i++) {
//            arrayOfByte2[i] = (byte) (i + 122 - 2*b[i]);
//        }
//
//        return new String(arrayOfByte2);
//    }
//
//    public static String check(String paramString)
//    {
//        byte[] arrayOfByte1 = paramString.getBytes();
//        byte[] arrayOfByte2 = new byte[16];
//        int i = 0;
//        while (i < 16)
//        {
//            arrayOfByte2[i] = ((byte)((arrayOfByte1[i] + b[i]) % 61));
//            i += 1;
//        }
//        i = 0;
//        while (i < 16)
//        {
//            arrayOfByte2[i] = ((byte)(arrayOfByte2[i] * 2 - i));
//            i += 1;
//        }
//        return new String(arrayOfByte2);
//    }

    public static String re() {

    }


}
