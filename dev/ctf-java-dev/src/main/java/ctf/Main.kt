package ctf

import kotlin.experimental.xor

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

    val s = byteArrayOf(
            113, 123, 118, 112, 108, 94, 99, 72, 38, 68,
            72, 87, 89, 72, 36, 118, 100, 78, 72, 87,
            121, 83, 101, 39, 62, 94, 62, 38, 107, 115,
            106)
    for (b in s) {
        print(b.xor(0x17).toChar())
    }

}
