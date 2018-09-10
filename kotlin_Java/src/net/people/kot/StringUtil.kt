package net.people.kot

import java.security.MessageDigest


fun applySha256(input: String): String {
    val digest = MessageDigest.getInstance("SHA-256")
    val hash = digest.digest(input.toByteArray(charset("UTF-8")))

    val hexstr = StringBuilder()
    for (hexb in hash) {
        val a = 0xff and hexb.toInt()
        val hex = Integer.toHexString(a)
        if (hex.length == 1) hexstr.append('0')
        hexstr.append(hex)
    }

    return hexstr.toString()
}