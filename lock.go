package main

import (
	base64 "encoding/base64"
	"fmt"
)

func main() {
	enctest := "teststring"

	encodedString := base64.StdEncoding.EncodeToString([]byte(enctest))
	fmt.Println(encodedString)
}
