package main

import (
	"tpath"
	"views"
	"fmt"
	//"github.com/imroc/biu"

	"io"
	"net/http"
	"log"

	"os"
	"strings"
	"net/url"

	"path/filepath"
)

var realPath *string

func main() {
	fmt.Printf("Hello,world, Sqrt(2) = %v\n", tpath.Sqrt(2))
	fmt.Printf("Hello,GO, VSqrt(2) = %v\n", views.VSqrt(3))

	// 开始go的学习
	firstDay()

	secDay();
	//a, b := swap(100, 200)
	//fmt.Printf("even: %v\n", even(a^b))
	//fmt.Printf("swap: %d\t%d\n", a, b)
	//fmt.Printf("shifting: %d\n", shifting(100))
	//fmt.Printf("nagation: %d\n", nagation(100))
	//
	//fmt.Println(biu.ToBinaryString(3))
	//fmt.Println(biu.ToBinaryString(int8(4)))
	//fmt.Println(biu.ToBinaryString(uint16(2)))
	//fmt.Println(biu.ToBinaryString([]byte{1, 2, 3}))
	//s := biu.BytesToBinaryString([]byte("xxxx.png"))
	//fmt.Println(s[1: len(s)-1])
	//fmt.Println(biu.ToBinaryString([]byte("zhangguo")))
	//
	//// 构建网络请求
	//
	//http.HandleFunc("/", dealStaticFiles)    //设置访问的路由
	//err := http.ListenAndServe(":9080", nil) //设置监听的端口
	//if err != nil {
	//	log.Fatal("ListenAndServe: ", err)
	//}

}
func secDay() {

	// map 属于引用类型 ， 新的 赋值 指向同一个内存的数据结构 函数中对 map 的任何修改，对于外部的调用都是可见的。
	personSalary := map[string]int{
		"steve": 12000,
		"jamie": 15000,
	}
	personSalary["mike"] = 9000
	fmt.Println("length is", len(personSalary))
	for key, value := range personSalary {
		fmt.Printf("personSalary  [%s] = %d\n", key, value)
	}

	fmt.Println("map before deletion", personSalary)
	delete(personSalary, "steve")
	fmt.Println("map after deletion", personSalary)
}

var StaticDir = "/static"

func getCurDir() string {
	dir, err := filepath.Abs(filepath.Dir(os.Args[0]))
	if err != nil {
		log.Fatal(err)
	}
	return strings.Replace(dir, "\\", "/", -1)
}

func dealStaticFiles(w http.ResponseWriter, r *http.Request) {
	stDir := getCurDir()

	if strings.HasPrefix(r.URL.Path, StaticDir) {
		file := stDir + r.URL.Path
		fmt.Println(file)
		f, err := os.Open(file)
		defer f.Close()

		if err != nil && os.IsNotExist(err) {
			fmt.Fprintln(w, "File not exist")
			return
		}
		http.ServeFile(w, r, file)
		return
	} else {
		fmt.Fprintln(w, "Hello world")
	}
}

func HelloServer(w http.ResponseWriter, req *http.Request) {
	io.WriteString(w, "hello world!\n")
	var par = req.URL.RawQuery
	fmt.Println(par)
	queryForm, err := url.ParseQuery(par)

	if err == nil && len(queryForm["a"]) > 0 {
		fmt.Println(queryForm["a"])
	}

}

// 获取0-n之间的所有偶数
func even(a int) (array []int) {
	fmt.Printf("a异或b:%d\n", a)
	for i := 0; i < a; i++ {
		if i&1 == 0 { // 位操作符&与C语言中使用方式一样
			array = append(array, i)
		}
	}
	return array
}

// 互换两个变量的值
// 不需要使用第三个变量做中间变量
func swap(a, b int) (int, int) {
	a ^= b // 异或等于运算
	b ^= a
	a ^= b
	return a, b
}

// 左移、右移运算
func shifting(a int) int {
	a = a << 1
	a = a >> 1
	return a
}

// 变换符号
func nagation(a int) int {
	// 注意: C语言中是 ~a+1这种方式
	return ^a + 1 // Go语言取反方式和C语言不同，Go语言不支持~符号。
}

func firstDay() {

	fmt.Print("开始Go的学习")
	fmt.Print("开始学习go语言的 函数 -----> ")

	a := 1
	b := 2
	c := true
	//d := "abc"
	//a, b, c = swapDay(a, b,c, d)

	fmt.Printf("%d %d", a, b)

	fmt.Println(c)

	// add 方法中的的运算 不会影响到a的值
	add(a)
	fmt.Printf("传值:%d", a)
	// 传入指针
	fmt.Println()
	add1(&a)
	fmt.Printf("传指针:%d", a)
	fmt.Println()
	// 接口
	var animal Animal
	animal = new(Bird)

	animal.fly()
	animal.run()
}

func swapDay(a, b int, c bool, d string) (int, int, bool) {

	fmt.Println(c, d)
	return b, a, a == b
}

func add(a int) (int) {
	a = a + 1;
	return a;
}
func add1(a *int) (*int) {
	*a = *a + 1;
	return a;
}

type Animal interface {
	fly()
	run()
}

type Bird struct {
}

func (bird Bird) fly() {
	fmt.Println("i can fly ")
}
func (bird Bird) run() {
	fmt.Println("i don,t like run ")
}
