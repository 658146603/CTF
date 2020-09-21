package test

import java.util.*
import kotlin.experimental.xor

fun main() {
    println("helloworld")
    println(CTF_JAVA.i())

    val flag = "hacking_for_fun}".toCharArray()
    flag.forEachIndexed { i, c ->
        if (flag[i] == 'i' || flag[i] == 'r') {
            flag[i] = '1'
        }
    }
    println(String(flag))

    val xor = byteArrayOf(
            0x66, 0x0a, 0x6b, 0x0c, 0x77, 0x26, 0x4f, 0x2e, 0x40, 0x11, 0x78, 0x0d, 0x5a, 0x3b, 0x55, 0x11, 0x70, 0x19, 0x46, 0x1f, 0x76, 0x22, 0x4d, 0x23, 0x44, 0x0e, 0x67, 0x06, 0x68, 0x0f, 0x47, 0x32, 0x4f
    )
    for (i in 0 until xor.size - 1)
        xor[xor.size - i - 1] = xor[xor.size - i - 1] xor xor[xor.size - i - 2]
    println(String(xor))


    val re3 = "e3nifIH9b_C@n@dH".toCharArray()
    for (index in re3.indices) {
        re3[index] = re3[index].minus(index)
    }
    println(String(Base64.getDecoder().decode(String(re3))))


    val key = intArrayOf(
            180, 136, 137, 147, 191, 137, 147, 191, 148, 136,
            133, 191, 134, 140, 129, 135, 191, 65)

    key.forEach {
        print((it-64 xor 0x20).toChar())
    }
    println()


}
