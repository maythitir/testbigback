package main

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"strings"
)

type Employee struct {
	ID   string `json:"ID"`
	Name string `json:"Name"`
	Age  string `json:"Age"`
	Team string `json:"Team"`
}

func getCSVFilePath(id string) string {
	return fmt.Sprintf("%s.csv", id)
}

func readCSVFile(filePath string) ([]Employee, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	reader := csv.NewReader(file)

	var employees []Employee

	// Read and parse CSV content
	lines, err := reader.ReadAll()
	if err != nil {
		return nil, err
	}
	// Remove the header row
	lines = lines[1:]

	// Create employees array
	for _, line := range lines {
		employee := Employee{
			ID:   line[0],
			Name: line[1],
			Age:  line[2],
			Team: line[3],
		}

		employees = append(employees, employee)
	}

	return employees, nil
}

func handleCSVRequest(w http.ResponseWriter, r *http.Request) {
	// Extract the {id} from the path parameter
	id := strings.TrimPrefix(r.URL.Path, "/file/")

	// Get the file path for the given id
	filePath := getCSVFilePath(id)
	// id=employee filePath=employee.csv
	// Read and parse the CSV file
	employees, err := readCSVFile(filePath)
	if err != nil {
		http.Error(w, "File not found", http.StatusNotFound)
		return
	}

	// Respond in JSON format
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]interface{}{
		"code": "success",
		"data": map[string]interface{}{
			"total":   len(employees),
			"records": employees,
		},
	})
}

func main() {
	http.HandleFunc("/file/", handleCSVRequest)

	// Run the server on port 8080 http://localhost:8080/file/employee
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println("Error starting the server:", err)
	}
}
