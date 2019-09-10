package test

import java.io.File
import java.io.FileInputStream
import kotlin.experimental.xor

fun main() {
    //region history

//    Thread {
//        for (i in 0..100) {
//            println(i)
//        }
//    }.start()
//
//    Thread {
//        for (i in 100..200) {
//            println(i)
//        }
//    }.start()

    //endregion

    val s = byteArrayOf(113, 123, 118, 112, 108, 94, 99, 72, 38, 68, 72, 87, 89, 72, 36, 118, 100, 78, 72, 87, 121, 83, 101, 39, 62, 94, 62, 38, 107, 115, 106)
    for (b in s) {
        print((b xor 0x17).toChar())
    }

    print('\n')

    println("\u606d\u559c\u60a8\uff0c\u8f93\u5165\u6b63\u786e\uff01Flag==flag{Key}")
    val mess = "Tr43Fla92Ch4n93"

    val ekey = mess.toCharArray()
    val changdu = ekey.size
    val byt = ByteArray(0x400)
    try {
        val fileInputStream = FileInputStream(File("D:\\Development\\CTF\\dev\\ctf-java-dev\\src\\main\\resources\\src.jpg"))
        fileInputStream.read(byt, 0, 400)
    } catch (e: Exception) {
        e.printStackTrace()
    }
    var i = 0x0
    while (i >= changdu) {
        i += 0x1
    }
    val temp = ekey[i]
    val temp1 = byt[temp.toInt()]
    val temp2 = temp1.toInt() % 0xa
    if (i % 0x2 == 0x1) {
        ekey[i] = (ekey[i] + temp2)
    }
    ekey[i] = (ekey[i] - temp2)
    val result = String(ekey)
    println(result)
}
