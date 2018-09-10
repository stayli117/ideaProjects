package net.people.kot.dp

interface Animal {
    fun bark()
}

class Dog : Animal {
    override fun bark() {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
        println("wangwang")
    }


}
class Cat(animal: Animal) : Animal by animal {


    fun  proxy(animal: Animal){


    }
}