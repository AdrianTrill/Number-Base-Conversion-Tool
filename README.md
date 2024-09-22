---

# **Number Base Conversion Tool**

A comprehensive **Python application** designed for converting numbers between different bases (binary, octal, decimal, hexadecimal, etc.) using various methods such as rapid conversion, substitution, and successive divisions. The project includes a command-line interface (CLI) for performing conversions, basic arithmetic operations on numbers in any base, and unit tests to ensure accuracy and reliability.

---

## **Project Overview**

This project implements various number base conversion techniques with robust validation and error handling, making it ideal for educational purposes, coding challenges, or development of more complex systems requiring number base conversions.

### **Key Features**
- **Multiple Conversion Methods**: Convert numbers between any two bases (2 to 16) using:
  - **Rapid conversion** (binary to/from other bases like octal and hexadecimal).
  - **Substitution method** (source to destination base).
  - **Successive divisions**.
  - **Base 10 intermediary conversion**.
- **Arithmetic Operations**: Perform addition, subtraction, multiplication, and division between numbers in any base.
- **Command-line Interface**: Intuitive CLI to guide users through conversions and operations.
- **Validation**: Comprehensive checks to ensure valid inputs and correct base representations.
- **Unit Testing**: Extensive test cases for all major operations to guarantee functionality and reliability.

---

## **Project Structure**

```bash

📁 ConversionMethods/                # Core conversion logic
   └── ConversionMethods.py          # Methods for rapid, substitution, successive divisions, and intermediary conversions.

📁 CheckStatements/                  # Input validation and utility functions
   └── CheckStatements.py            # Functions to validate bases, numbers, and conversion feasibility.

📁 ConversionUI/                     # User interface (CLI)
   └── ConversionUI.py               # Interface for performing base conversions and arithmetic operations.

📁 DataTests/                        # Unit tests
   └── DataTests.py                  # Test cases for conversion methods and base operations.

📁 NumberBaseOperations/             # Base arithmetic operations
   └── NumberBaseOperations.py       # Add, subtract, multiply, divide numbers in different bases.

📁 ProgramRunFile/                   # Main entry point for the program
   └── ProgramRunFile.py             # Runs the program through the CLI.

📁 resources/                        # Additional resources
   └── Documentation.docx            # Project documentation with detailed explanations.

```

---

## **Conversion Methods**

### **1. Rapid Conversion** 
Convert numbers between binary, octal, hexadecimal, and other bases using the grouping method.

### **2. Substitution Method** 
Convert numbers by representing the number as a sum of powers of the base.

### **3. Successive Divisions** 
Convert numbers by repeated division by the target base and recording the remainders.

### **4. Base 10 Intermediary**
Convert numbers first to base 10 and then to the desired base.

---

## **Getting Started**

### **Prerequisites**
- Python 3.x
- Clone or download the project repository.

```bash
git clone https://github.com/your-github-repo/number-base-conversion.git
cd number-base-conversion
```

### **Running the Program**

1. Navigate to the project directory.
2. Run the program using the CLI interface.
```bash
python ProgramRunFile.py
```

### **Usage**

Upon running the program, follow the CLI instructions to:
- Convert numbers between different bases.
- Perform arithmetic operations (addition, subtraction, multiplication, division) on numbers in any base.

### **Running Tests**
Unit tests can be executed to verify the functionality of the conversion methods and base operations:
```bash
python -m unittest DataTests.py
```

---

## **Technologies Used**

- **Python**: Core programming language used for the project.
- **Unit Testing**: Built-in Python library to validate conversion logic.
- **CLI**: Command-line interface for user interaction.

---

## **Future Enhancements**

- **GUI Integration**: Plan to extend the project with a graphical user interface for easier interactions.
- **Support for Higher Bases**: Extend support for bases greater than 16.
- **Advanced Mathematical Operations**: Addition of more complex operations such as exponentiation and modular arithmetic in any base.

---

## **Contributing**

Contributions are welcome! Feel free to fork this project, submit issues, or create pull requests. Please ensure your changes are well-documented and thoroughly tested.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Contact**

For any queries or further discussions, feel free to reach out.

---

### **Developer**
**Mititean Adrian**  
*Computer Science Student | Babes-Bolyai University*

---

## **Resume Integration**

### **Projects**
**Number Base Conversion Tool**  
*GitHub*: [https://github.com/your-github-repo/number-base-conversion](https://github.com/your-github-repo/number-base-conversion)

- Designed and implemented a Python tool for converting numbers between any two bases (2 to 16), supporting rapid conversion, substitution, and successive division methods.
- Developed a command-line interface to guide users through conversions and base operations.
- Implemented robust input validation and error handling to ensure accuracy and reliability.
- Created unit tests for core functions, ensuring precision and stability of the conversion logic.
- Technology stack: Python, CLI, Unit Testing.

This project demonstrates my skills in Python programming, problem-solving, and building efficient, user-friendly software solutions. I applied concepts of algorithms, data structures, and arithmetic operations while creating a practical, real-world tool for base conversions.

---
