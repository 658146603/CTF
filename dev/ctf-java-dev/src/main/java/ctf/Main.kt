package ctf

import ctf.crypto.Brainfuck
import ctf.crypto.NetUtils

fun main() {
//    val str = readLine()
//    print(Brainfuck.parse(str))
//    print(str?.reversed())

//    print(CTF1.getFlag())

//    val url = "http://96024d41-0452-4b32-b6c9-a48392d4c450.node1.buuoj.cn/info/"
//
//    Thread(Runnable {
//        for(i in 1600..1800) {
//            val result = NetUtils.get(url + i)
//            println(i)
//            if ("lv6" in result) {
//                println(result)
//                break
//            }
//        }
//    }).run()
//
//    Thread(Runnable {
//        for(i in 1400..1600) {
//            val result = NetUtils.get(url + i)
//            println(i)
//            if ("lv6" in result) {
//                println(result)
//                break
//            }
//        }
//    }).run()

    val a = arrayOf<Byte>(21, -93, -68, -94, 86, 117, -19, -68, -92, 33,
            50, 118, 16, 13, 1, -15, -13, 3, 4, 103,
            -18, 81, 30, 68, 54, -93, 44, -23, 93, 98,
            5, 59)

    print(a)

}
