package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func maxPairwiseProductFaster(numbers []int) float64 {
	biggest := 0.0
	secondBiggest := 0.0
	for _, number := range numbers {
		if number > int(biggest) {
			if biggest > secondBiggest {
				secondBiggest = biggest
			}
			biggest = float64(number)
		} else {
			if number > int(secondBiggest) {
				secondBiggest = float64(number)
			}
		}
	}
	return biggest * secondBiggest
}

func main() {

	reader := bufio.NewReader(os.Stdin)

	var totalNumbers int
	_, err := fmt.Scanf("%d", &totalNumbers)
	if err != nil {
		fmt.Print(err)
	}

	values, _ := reader.ReadString('\n')

	valuesArray := strings.Fields(values)

	intArray := []int{}
	for i := 0; i < totalNumbers; i++ {
		i, _ := strconv.Atoi(valuesArray[i])
		intArray = append(intArray, i)
	}

	result := maxPairwiseProductFaster(intArray)

	fmt.Printf("%.0f", result)
}

//-------------------------------------------------------------------------
// package main

// import (
// 	"bufio"
// 	"fmt"
// 	"math"
// 	"os"
// 	"strconv"
// 	"strings"
// )

// func maxPairwiseProduct(numbers []int) float64 {
// 	maxProduct := 0.0

// 	for first, _ := range numbers {
// 		for second := first + 1; second < len(numbers); second++ {
// 			maxProduct = math.Max(float64(maxProduct),
// 				float64(numbers[first]*numbers[second]))
// 		}
// 	}
// 	return maxProduct
// }

// func maxPairwiseProductFaster(numbers []int) float64 {
// 	biggest := 0.0
// 	secondBiggest := 0.0
// 	for _, number := range numbers {
// 		if number > int(biggest) {
// 			if biggest > secondBiggest {
// 				secondBiggest = biggest
// 			}
// 			biggest = float64(number)
// 		} else {
// 			if number > int(secondBiggest) {
// 				secondBiggest = float64(number)
// 			}
// 		}
// 	}
// 	return biggest * secondBiggest
// }

// func main() {

// 	reader := bufio.NewReader(os.Stdin)
// 	values, _ := reader.ReadString('\n')

// 	valuesArray := strings.Fields(values)

// 	fmt.Printf("Values splitted: %v\n", valuesArray)

// 	intArray := []int{}
// 	for _, v := range valuesArray {
// 		i, _ := strconv.Atoi(v)
// 		intArray = append(intArray, i)
// 	}

// 	result := maxPairwiseProduct(intArray)

// 	fmt.Print(result)

// 	var n int
// 	var values []int

// 	nInt := int

// 	fmt.Printf("Go ------------------------------------ \n")
// 	for {
// 		n := rand.Intn(10000)
// 		values := rand.Perm(n)

// 		if len(values) < 8000 {
// 			continue
// 		}

// 		fmt.Printf("Total values: %d\n", len(values))

// 		start_max := time.Now()
// 		max := maxPairwiseProduct(values[:])
// 		elapsed_max := time.Since(start_max).Nanoseconds()
// 		fmt.Printf("Max Common took: %v\n", elapsed_max)

// 		start_faster := time.Now()
// 		max_faster := maxPairwiseProductFaster((values[:]))
// 		elapsed_faster := time.Since(start_faster).Nanoseconds()
// 		fmt.Printf("Max Faster took: %v\n", elapsed_faster)

// 		// fmt.Printf("Max value is: %.1f\n", max)
// 		// fmt.Printf("Max Faster value is: %.1f\n", max_faster)
// 		// fmt.Printf("Values: %v\n", values)

// 		fmt.Printf("Max Faster is %.1dx faster than Max", int64(elapsed_max/elapsed_faster))

// 		fmt.Printf("\n-------------\n")
// 		if max != max_faster {
// 			fmt.Printf("Max is: %.1f", max)
// 			fmt.Printf("Max Faster is: %.1f", max_faster)
// 			break
// 		}
// 	}
// }
