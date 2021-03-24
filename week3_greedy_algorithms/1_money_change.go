package main

import (
  "fmt"
  )

func getChange(m int) int {
  current := m;
  changes := 0;

  changes += current / 10;
  current = current % 10;

  changes += current / 5;
  current = current % 5;

  changes += current / 1;
  current = current % 1;

  return changes;
}

func main() {
	var m int
	_, err := fmt.Scanf("%d", &m)
	if err != nil {
		fmt.Print(err)
	}

  fmt.Print(getChange(m))

}