package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net"
	"os"
	"io"
	"os/signal"
	"github.com/Jailman/protocol"

	"./stream"
	"./websocket_handler"
	// "strconv"
	// "net/http"
	// "github.com/gorilla/handlers"
	"github.com/gorilla/mux"
)

// 控制机器人方向
func HandleRobotWheels(direction string) {

}

// rsapivid相关参数
const (
	staticDir         = "static"
	staticURL         = "/static"
	videoWebsocketURL = "/stream"
	port              = 8080
	width             = 960
	height            = 540
	fps               = 30
)

// 开启视频流并监听
func HandleVideoStream(conn net.Conn) {

	options := stream.CameraOptions{
		Width:          width,
		Height:         height,
		Fps:            fps,
		HorizontalFlip: true,
		VerticalFlip:   true,
		Rotation:       0,
	}

	router := mux.NewRouter()

	// Websocket
	connectionNumber := make(chan int, 2)
	wsh := websocket_handler.NewWebSocketHandler(connectionNumber)
	router.HandleFunc(videoWebsocketURL, wsh.Handler)
	go stream.Video(options, wsh, connectionNumber)

	// Static
	// fs := http.FileServer(http.Dir(staticDir))
	// router.PathPrefix(staticURL).Handler(handlers.CompressHandler(http.StripPrefix(staticURL, fs)))
	// log.Fatal(http.ListenAndServe(":"+strconv.Itoa(port), router))

}

// 温度传感器
func HandleTemperature() float64 {
	return 0
}

// 湿度传感器
func HandleHumidity() float64 {
	return 0
}

// 语音交互
func handleVoiceInteraction() {

}

// 自动避障
func AvoidObstacle() {

}

// 自动巡线充电
func AutoCharge() {

}


// Socket通信函数
// 发送消息
func handleConnection_SendMission(conn net.Conn, mission string) {

	conn.Write(protocol.Enpack([]byte(mission)))
	Log(mission)
	Log("Mission sent.")
	// defer conn.Close()

}

func handleConnection_getStatus(conn net.Conn) {

	// 缓冲区，存储被截断的数据
	tmpBuffer := make([]byte, 0)

	// 接收解包
	readerChannel := make(chan []byte, 16)
	go reader(readerChannel, conn)

	buffer := make([]byte, 1024)
	for {
		n, err := conn.Read(buffer)
		if err != nil {
			if err == io.EOF {
				Log("Client disconnected.")
			} else {
				Log(conn.RemoteAddr().String(), " connection error: ", err)
			}
			return
		}

		tmpBuffer = protocol.Depack(append(tmpBuffer, buffer[:n]...), readerChannel)
	}
	// defer conn.Close()

}

// 读取channel中的消息并作出相应的操作和回应
func reader(readerChannel chan []byte, conn net.Conn) {
	for {
		select {
		case data := <-readerChannel:
			var dat map[string]interface{}
			if err := json.Unmarshal([]byte(string(data)), &dat); err == nil {

				if dat["Mission"].(string) == "heartbeat" {
					if dat["Status"].(string) == "check" {
						Log(conn.RemoteAddr().String(), "heartbeat check.")
						mission := "{\"Mission\":\"heartbeat\", \"Status\":\"ok\"}"
						handleConnection_SendMission(conn, mission)
					}
				} else {
					Log(conn.RemoteAddr().String(), "receive: ", dat["Mission"], " ", dat["Status"])
				}
			} else {
				log.Fatal(err)
			}
		}
	}
}

// log打印消息
func Log(v ...interface{}) {
	log.Println(v...)
}

// 错误检查
func CheckError(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
		os.Exit(1)
	}
}

// 手动中断
func listenSigInt() chan os.Signal {
	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, os.Kill)
	return c
}

// main函数
func main() {

	// 手动终止
	go func() {
		quitChan := listenSigInt()
		select {
		case <-quitChan:
			log.Printf("got control-C")
			os.Exit(0)
		}
	}()

	// 建立socket，监听端口
	listen := ":8888"
	netListen, err := net.Listen("tcp", listen)
	CheckError(err)
	defer netListen.Close()

	Log("Waiting for clients")
	
	// 向client发送命令
	for {
		conn, err := netListen.Accept()
		if err != nil {
			continue
		}

		Log(conn.RemoteAddr().String(), " tcp connect success")
		go handleConnection_getStatus(conn)
	}
}