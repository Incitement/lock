package main

import "fmt"
import base64 "encoding/base64"

func main() {
	enctest := "teststring"

	encodedString := base64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println(encodedString)
}