package ctf.crypto;

import java.util.HashMap;
import java.util.Stack;

public class Brainfuck {

    private static HashMap<Integer, Character> cs = new HashMap<>();//Code Segment
    private static HashMap<Integer, Character> ds = new HashMap<>();//Data Segment
    private static HashMap<Integer, Integer> sslr = new HashMap<>();//Stack Segment i -> ]
    private static HashMap<Integer, Integer> ssrl = new HashMap<>();//Stack Segment i -> [
    private static Stack<Integer> ssStack = new Stack<>();//Stack Segment []
    private static Integer bp = 0, readInBasePoint = 0, codeSegmentPoint = 0;//Base Point | args[1] readIn Point | Code Segment Point
    private static String result = "";

    //仅支持ASCII字符
    public static String parse(String codeSeg) {
        try {
            int whileNum = 0, left;
            for (Integer i = 0; i < codeSeg.length(); i++) {
                char c = codeSeg.charAt(i);
                cs.put(i, c);
                switch (c) {
                    case '[':
                        ssStack.push(i);
                        whileNum++;
                        break;
                    case ']':
                        whileNum--;
                        left = ssStack.pop();
                        sslr.put(left, i);
                        ssrl.put(i, left);
                        break;
                }
            }
            if (whileNum != 0) throw new BFException("BF异常 ：括号匹配错误 : whileNum = " + whileNum);
            while (codeSegmentPoint < cs.size()) {
                vm(cs.get(codeSegmentPoint));
            }
            return result;
        } catch (Exception e) {
            e.printStackTrace();
            return e.getMessage();
        }
    }

    private static void vm(Character c) throws Exception {
        switch (c) {
            case '+':
                plus();
                codeSegmentPoint++;
                break;
            case '-':
                des();
                codeSegmentPoint++;
                break;
            case '.':
                output();
                codeSegmentPoint++;
                break;
            case ',':
                read();
                codeSegmentPoint++;
                break;
            case '>':
                bp++;
                codeSegmentPoint++;
                break;
            case '<':
                bp--;
                if (bp == -1) {
                    throw new BFException("BF异常 ：指针越界 : bp = -1" + ".");
                }
                codeSegmentPoint++;
                break;
            case '[':
                whileLeft();
                break;
            case ']':
                whileRight();
                break;
            default:
                throw new BFException("BF异常: 输入错误: 未知字符 = '" + cs.get(codeSegmentPoint) + "' at " + codeSegmentPoint + ".");
        }
    }

    //数据+1
    private static void plus() {
        if (ds.containsKey(bp)) {
            int c = ds.get(bp) + 1;
            if (c == 256) {
                ds.put(bp, (char) 0);
            } else {
                ds.put(bp, (char) c);
            }
        } else {
            ds.put(bp, (char) 1);
        }
    }

    //数据-1
    private static void des() {
        if (ds.containsKey(bp)) {
            int c = ds.get(bp) - 1;
            if (c == -1) {
                ds.put(bp, (char) 255);
            } else {
                ds.put(bp, (char) c);
            }
        } else {
            ds.put(bp, (char) 255);
        }
    }

    //输出
    private static void output() throws BFException {
        if (ds.containsKey(bp)) {
            result += ds.get(bp);
        } else {
            throw new BFException("BF异常 ：指针越界 : 数据不存在  : bp = " + bp + ".");
        }
    }

    //读入
    private static void read() throws BFException {
        if (readInBasePoint == -1) {
            throw new BFException("BF异常 ：数据不存在越界 : 请先输入数据.");
        } else {
            try {
                String readIn = "";
                ds.put(bp, readIn.charAt(readInBasePoint++));
            } catch (Exception e) {
                throw new BFException("BF异常 ：指针越界 : 输入数据长度不足 : readInbp = " + readInBasePoint + ".");
            }
        }

    }

    //循环右括号
    private static void whileRight() throws BFException {
        if (!ds.containsKey(bp)) {
            throw new BFException("BF异常 ：指针越界 : 循环检测空值: bp = " + bp + ".");
        } else {
            if (ds.get(bp) != 0) {
                codeSegmentPoint = ssrl.get(codeSegmentPoint);
                return;
            }
            codeSegmentPoint++;
        }
    }

    //循环左括号
    private static void whileLeft() throws BFException {
        if (!ds.containsKey(bp)) {
            throw new BFException("BF异常 ：指针越界 : 循环检测空值: bp = " + bp + ".");
        } else {
            if (ds.get(bp) == 0) {
                codeSegmentPoint = sslr.get(codeSegmentPoint);
                return;
            }
            codeSegmentPoint++;
        }
    }

    //自定义异常类
    static class BFException extends Exception {
        BFException(String msg) {
            super(msg);
        }
    }
}
