# Flask Quiz Application

This project is a simple web-based quiz application built using Flask. Users can answer questions of different types (single-choice and multiple-choice) and receive a score upon completion. The application reads questions from a JSON file, tracks user progress, and calculates the score based on user responses.

## Features

- Supports single-choice and multiple-choice questions
- Tracks user progress through sessions
- Calculates and displays user scores
- Easy to extend and customize

## Prerequisites

- Python 3.x
- Flask

## Getting Started

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/flask-quiz-app.git
    cd flask-quiz-app
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Ensure you have your questions file in the `data` directory:
    ```json
    // data/questions.json
    [
    {
        "question": "A company plans to use an Amazon Snowball Edge device to transfer files to the AWS Cloud. Which activities related to a Snowball Edge device are available to the company at no cost?",
        "type": "single",
        "options": [
            "A. Use of the Snowball Edge appliance for a 10-day period",
            "B. The transfer of data out of Amazon S3 and to the Snowball Edge appliance",
            "C. The transfer of data from the Snowball Edge appliance into Amazon S3",
            "D. Daily use of the Snowball Edge appliance after 10 days"
        ],
        "answer": "C. The transfer of data from the Snowball Edge appliance into Amazon S3"
    },
    {
        "question": "A company has deployed applications on Amazon EC2 instances. The company needs to assess application vulnerabilities and must identify infrastructure deployments that do not meet best practices. Which AWS service can the company use to meet these requirements?",
        "type": "single",
        "options": [
            "A. AWS Trusted Advisor",
            "B. Amazon Inspector",
            "C. AWS Config",
            "D. Amazon GuardDuty"
        ],
        "answer": "B. Amazon Inspector"
    }
    ]
    ```

2. Run the Flask application:
    ```bash
    flask run
    ```

3. Open your web browser and navigate to `http://127.0.0.1:8080/` to start the quiz.

## Project Structure
```
flask-quiz-app/
│
├── data/
│ └── questions.json # JSON file containing quiz questions
│
├── templates/
│ ├── base.html # Base template
│ ├── index.html # Homepage template
│ ├── quiz.html # Quiz page template
│ └── result.html # Result page template
│
├── static/
│ └── style.css # Base styles
│
├── .gitignore # Git ignore file
├── app.py # Main application script
├── requirements.txt # Python package dependencies
└── README.md # Project README file
```
## Contribution

Contributions are welcome! If you have any improvements or suggestions, please create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy quizzing!
