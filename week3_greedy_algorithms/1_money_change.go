package main

import (
  "fmt"
  )

func getChange(m int) int {
  return m;
}

func main() {
	var m int
	_, err := fmt.Scanf("%d", &m)
	if err != nil {
		fmt.Print(err)
	}

  fmt.Print(getChange(m))

}