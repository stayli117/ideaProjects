package net.people.kot

import com.google.gson.Gson
import net.people.kot.dp.Cat
import net.people.kot.dp.Dog


fun main(args: Array<String>) {
    println("hello world")
    Greeter("abc").greet()


    val genesisBlock = Block("Hi im the first block", "0");
    val secondBlock = Block("Yo im the second block", genesisBlock.mHash);
    val thirdBlock = Block("Hey im the third block", secondBlock.mHash);

    val list = listOf<Block>(genesisBlock, secondBlock, thirdBlock)

    val gson = Gson();
    val json = gson.toJson(list)
    println(json)


    // 动态代理实现

    Dog().bark()

    Cat(Dog()).proxy(Dog())

}

class Greeter(val name: String) {
    fun greet() {
        println("Hello , $name")
    }

    fun sendSystemInfo() {
        var userId = 13;
        val phoneNum = "18567677596"
        var registrationIds = "190&agdg&135"
        var arrayStr: Array<String> = arrayOf("abc", "bcd", "adhg")
        val list: List<String> = registrationIds.split("&")
    }
}